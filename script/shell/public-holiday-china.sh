#!/bin/bash

set -e

script_path=$(
  cd "$(dirname $0)"
  pwd
)

pushd ${script_path}

source ../venv/bin/activate

mkdir -p ../../docs/public-holiday

python3 ../python/holiday_ics_parser.py \
  --output-file=../../docs/public-holiday/china.ics \
  --config-dir=../../config/public-holiday/china

deactivate

popd
