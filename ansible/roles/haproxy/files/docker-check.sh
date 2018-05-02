#!/bin/bash
docker run -t \
           -v /etc/haproxy:/usr/local/etc/haproxy:ro \
           -v /dev/log:/dev/log \
           --name haproxy-check \
           --rm \
           haproxy:1.8.8 \
           haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg
