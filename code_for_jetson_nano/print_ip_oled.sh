#!/bin/bash
ip="$(ifconfig | grep -A 1 'wlan0' | tail -1 | cut -d ':' -f 2 | tr ' ' '-')";
ip=${ip:13:13}

python3 ~/FATEC_TCC_2022/code_for_jetson_nano/print_ip_oled.py $ip
