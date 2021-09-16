#!/bin/bash
python3 get_update.py && \
sudo dpkg -i plexmediaserver.deb && \
sudo apt-get install -f && \
rm -rf plexmediaserver.deb
