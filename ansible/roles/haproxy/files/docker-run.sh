#!/bin/bash
docker run -d \
           -v /etc/haproxy:/usr/local/etc/haproxy:ro \
           -v /dev/log:/dev/log \
           --name haproxy \
           --network host \
           --restart always \
           haproxy:1.8.8
