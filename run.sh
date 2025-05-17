#!/bin/sh

set -euo pipefail

cd $(dirname $0)
python3 -m venv venv
./venv/bin/pip3 install .
exec ./venv/bin/grafonix
