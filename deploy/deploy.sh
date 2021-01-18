#!/bin/sh
# Deploys to Fargate
set -o errexit

DOCKER_IMAGE=$1
ENV_NAME=$2

if [ -z ${DOCKER_IMAGE} ] || [ -z ${ENV_NAME} ]; then
  echo "usage: $0 (DOCKER_IMAGE) (ENV_NAME)"
  exit 1
fi

ENVCONFIG="./${ENV_NAME}env.sh"

if [ ! -f ${ENVCONFIG} ]; then
  echo "Missing envconfig file: ${ENVCONFIG}"
  exit 1
fi

source ${ENVCONFIG}

if [ -z ${EXECUTION_ROLE_ARN} ]; then
  echo "Missing required env var EXECUTION_ROLE_ARN. This should be defined in the config file ${ENVCONFIG}"
  exit 1
fi

if [ -z `which envsubst` ]; then
  echo "Please install envsubst"
  exit 1
fi

if [ -z `which aws` ]; then
  echo "Please install the aws cli"
  exit 1
fi

if [ -z `which jq` ]; then
  echo "Please install jq"
  exit 1
fi

DOCKER_IMAGE=${DOCKER_IMAGE} ENV_NAME=${ENV_NAME} MONGODB_NAME=${MONGODB_NAME} CLIENT_ID=${CLIENT_ID} \
  envsubst < taskdefinition.json > taskdefinition-${ENV_NAME}.json

NEW_DEFINITION=$(aws ecs register-task-definition --region "us-east-1" --cli-input-json file://taskdefinition-${ENV_NAME}.json)

NEW_REVISION=$(echo ${NEW_DEFINITION} | jq '.taskDefinition.revision')


echo "Deploy revision ${NEW_REVISION}..."

AWS_PAGER="" aws ecs update-service --cluster snowball-${ENV_NAME} \
                       --service snowball-${ENV_NAME} \
                       --task-definition snowball-${ENV_NAME}:${NEW_REVISION}

echo "Deployment requested"

rm taskdefinition-${ENV_NAME}.json