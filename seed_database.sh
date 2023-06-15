#!/bin/bash

rm db.sqlite3
rm -rf ./artbexapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations artbexapi
python3 manage.py migrate artbexapi
python3 manage.py loaddata category
python3 manage.py loaddata image
python3 manage.py loaddata artbex
python3 manage.py loaddata artbex_image

