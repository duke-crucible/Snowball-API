# -- BUILD --
FROM python:3.8.6-slim-buster AS build
WORKDIR /code

# Install build deps, then run `pip install`
RUN set -ex \
  && BUILD_DEPS=" \
  build-essential \
  libpq-dev \
  " \
  && apt-get update \
  && apt-get install -y --no-install-recommends $BUILD_DEPS \
  && apt-get upgrade -y \
  && apt-get install -y curl

RUN curl -SLO https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem

RUN pip install -U pip
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# -- DEPLOY --
FROM python:3.8.6-slim-buster AS deploy
WORKDIR /code

RUN apt-get update \
    && apt-get upgrade -y

# copy all the built python packages to the deployment container (no build deps)
COPY --from=build /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=build /code/rds-combined-ca-bundle.pem /code/rds-combined-ca-bundle.pem

COPY . /code/

# Drop root privileges within the container. From:
# https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b
RUN groupadd -g 999 appuser && \
  useradd -r -d /code -u 999 -g appuser appuser && \
  chown appuser:appuser -R /code
USER appuser

EXPOSE 8000

ENV FLASK_APP ./run.py

CMD [ "gunicorn", \
  # See https://pythonspeed.com/articles/gunicorn-in-docker/ for worker settings.
  "--worker-tmp-dir=/dev/shm", \
  "--worker-class=gthread", \
  "--bind=0.0.0.0:8000", \
  "--threads=4", \
  "--workers=2", \
  "run:app"]
