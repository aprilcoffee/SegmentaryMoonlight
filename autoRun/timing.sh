#!bin/sh
# time.sh

cd /
sudo modprobe i2c-bcm2708
echo ds3231 0x68 | sudo tee /sys/class/i2c-adapter/i2c-1/new_device
sudo hwclock
sudo hwclock -s
exit 0
