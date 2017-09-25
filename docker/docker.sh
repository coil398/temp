docker pull ubuntu:16.04

if [ -e ./pepper ]; then
    echo 'folder pepper exists'
else
    mkdir pepper
fi

docker build -t pepper:python .

docker run -v $HOME/docker/pepper -it --name pepper pepper:python /bin/bash
