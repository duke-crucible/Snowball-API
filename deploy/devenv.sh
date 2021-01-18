#!/bin/sh
# Config for the dev environment

export EXECUTION_ROLE_ARN="arn:aws:iam::371341698719:role/ecs-snowball-dev-TaskExecutionRole"
export TASK_ROLE_ARN="arn:aws:iam::371341698719:role/ecs-snowball-dev-TaskRole"
export MONGODB_NAME="snowball-gr-dev-0"
export CLIENT_ID="snowball_gr_web_dev"
# TODO: create domain
# export BASE_URI="https://dev.snowball.dukecrucible.net"
