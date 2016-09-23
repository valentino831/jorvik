#!/bin/bash

rm -rf .venv
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt --upgrade

DBNAME="jorvik_$RANDOM"
TEST_DBNAME="test_$DBNAME"

# Use random name for the new database -- used for testing
sed "s/database = .*/database = $DBNAME/g" config/pgsql.cnf.sample > config/pgsql.cnf

psql -U postgres -c 'CREATE DATABASE $TEST_DBNAME;'
psql -U postgres -c "CREATE EXTENSION postgis" -d $TEST_DBNAME
psql -U postgres -c "CREATE EXTENSION postgis_topology" -d $TEST_DBNAME
pg_restore -O -d $TEST_DBNAME ./base/test_jorvik.pgsql -j 4
