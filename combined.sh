#!/data/data/com.termux/files/usr/bin/bash

# Install required packages
yes|pkg update && yes|pkg upgrade
pkg install cmake -y

# Install Python packages
pip3 install -r requirements.txt

# Exit with success
exit 0
