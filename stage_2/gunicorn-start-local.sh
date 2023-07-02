#!/bin/bash
gunicorn --chdir ./src -c gunicorn.conf.py
