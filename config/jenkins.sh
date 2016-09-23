#!/bin/bash

virtualenv --python=python3 .venv
source .venv/bin/activate
pip install pip wheel --force-reinstall
pip install -r requirements.txt --force-reinstall
