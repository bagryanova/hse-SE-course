#!/usr/bin/env bash
set -e

path="$1"

"$path" -m pip install virtualenv
"$path" -m virtualenv -p "$path" venv
source venv/bin/activate
python3 -m pip install fastapi[all]
python3 -m pip install -r requirements.txt
