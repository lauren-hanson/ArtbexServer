#!/bin/bash

rm db.sqlite3
rm -rf ./artbexapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations artbexapi
python3 manage.py migrate artbexapi
python3 manage.py loaddata creator
python3 manage.py loaddata tone
python3 manage.py loaddata audience
python3 manage.py loaddata format
python3 manage.py loaddata production
python3 manage.py loaddata artbex
# python3 manage.py loaddata artbexformat
# python3 manage.py loaddata artbexproduction
# python3 manage.py loaddata artbexaudience
