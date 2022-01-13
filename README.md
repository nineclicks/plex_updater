# Plex Updater

## Requirements
- A Debian based distro with dpkg, apt-get
- Python3

## Setup
```bash
pip3 install -r requirements.txt
cp config-example.json config.json
# Update config.json with host and token.
# https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
```

## Run
```bash
./updater.sh
# Script will check for update then download and install the update if found.
```