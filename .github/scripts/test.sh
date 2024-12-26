#!/bin/bash
sudo apt update -y
curl -fsSL https://get.docker.com -o /tmp/install-docker.sh
sudo sh /tmp/install-docker.sh
sudo usermod -aG docker ubuntu
