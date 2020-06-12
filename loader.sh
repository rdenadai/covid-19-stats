#!/bin/bash

cd /home/pi/projects/covid19statistics/

python loader.py

git add .

git commit -m "Automatic Update"

source .env

git push https://$GIT_USER:$GIT_PASSWD@github.com/rdenadai/covid-19-stats.git

export GIT_USER=
export GIT_PASSWD=
