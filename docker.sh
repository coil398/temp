#! /bin/sh

docker pull ubuntu:16.04
docker run -v $HOME/Documents/workspace/docker/ -it --name pepper ubuntu:16.04 /bin/bash
