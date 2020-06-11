#!/bin/bash

python3.8 init_schema.py
gunicorn -w 4 --bind 0.0.0.0:8080 start:app