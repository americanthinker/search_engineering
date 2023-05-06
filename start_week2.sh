#!/bin/bash

cd docker
docker-compose -f docker-compose-w2.yml up
cd ../docker-grafana
bash install-plugin.sh
docker-compose -f monitoring.yml up