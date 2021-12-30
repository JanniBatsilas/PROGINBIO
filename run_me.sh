#!/bin/bash

python src/execute_tasks.py
flake8 src/
coverage run --source src/ -m pytest && coverage report -m
