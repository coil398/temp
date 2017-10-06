#!/bin/sh

docker run -v $HOME/docker/pepper:/root/pepper -it --name pepper pepper:python /bin/bash
