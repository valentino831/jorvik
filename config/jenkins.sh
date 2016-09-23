#!/bin/bash

rm -rf .venv
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt --upgrade
