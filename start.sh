#!/bin/bash

systemctl status docker.service 
systemctl enable docker.service 
systemctl start docker.service 
systemctl status docker.service 

