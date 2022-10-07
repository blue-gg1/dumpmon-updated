#!/bin/bash
# 
# to do: make this in python

systemctl status docker.service 
systemctl enable docker.service 
systemctl start docker.service 
systemctl status docker.service 

docker start test-db
docker ps