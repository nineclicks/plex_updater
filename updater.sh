#!/bin/bash
python3 get_update.py && \
sudo dpkg -i plex_update.deb && \
sudo apt-get install -f && \
rm -rf plex_update.deb
