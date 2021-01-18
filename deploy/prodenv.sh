#!/bin/sh
# Config for the prod environment

export EXECUTION_ROLE_ARN="arn:aws:iam::371341698719:role/ecs-snowball-prod-TaskExecutionRole"
export TASK_ROLE_ARN="arn:aws:iam::371341698719:role/ecs-snowball-prod-TaskRole"
export MONGODB_NAME="snowball-gr-prod-0"
export CLIENT_ID="snowball_gr_web_prod"
# TODO: create domain for prod
# export BASE_URI="https://snowball.duhs.duke.edu"


