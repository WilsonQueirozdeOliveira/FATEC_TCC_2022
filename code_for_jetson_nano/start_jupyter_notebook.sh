#!/bin/bash
ip="$(ifconfig | grep -A 1 'wlan0' | tail -1 | cut -d ':' -f 2 | tr ' ' '-')";
ip=${ip:13:13}
echo "$ip"
jupyter notebook --ip "$ip" --port 8888

