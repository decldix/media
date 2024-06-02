#!/usr/bin/env bash

# VHS
# Debian/Ubuntu
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
# Install ttyd from https://github.com/tsl0922/ttyd/releases
sudo apt update && sudo apt install vhs ffmpeg  

# Slides
sudo snap install slides

# Toilet
sudo apt install toilet toilet-fonts

# other utils for the scripts
sudo apt install rename libxt-dev libxi-dev libgl-dev