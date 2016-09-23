#!/bin/bash

rm -rf .venv
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt --upgrade

# Use random name for the new database -- used for testing
sed "s/database = .*/database = jorvik$RANDOM/g" config/pgsql.cnf.sample > config/pgsql.cnf
