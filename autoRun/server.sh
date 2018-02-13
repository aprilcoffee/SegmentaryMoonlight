#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pi/Desktop/SegmentaryMoonlight/source

sudo modprobe i2c-bcm2708
echo ds3231 0x68 | sudo tee /sys/class/i2c-adapter/i2c-1/new_device
sudo hwclock
sudo hwclock -s
sudo python light2.py
cd ..
cd /
