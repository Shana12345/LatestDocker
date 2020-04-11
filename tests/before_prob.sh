#!/bin/bash

source /var/lib/jenkins/.bashrc

python3 -m coverage run pytest tests/testing.py

python3 -m coverage report -m