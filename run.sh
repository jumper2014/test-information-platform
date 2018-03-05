#!/usr/bin/env bash
nohup python manage.py runserver --host 0.0.0.0 --threaded > monitor.log 2>&1 &

