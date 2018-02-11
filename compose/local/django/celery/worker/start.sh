#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A intuitiveweb.taskapp worker -l INFO
