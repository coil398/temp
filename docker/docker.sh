if [ -e ./pepper ]; then
    echo 'folder pepper exists'
else
    mkdir pepper
fi

wget -O Dockerfile https://goo.gl/zyM4fk
docker build -t pepper:python .
# docker run -v $HOME/docker/pepper:/root/pepper -it --name pepper pepper:python /bin/bash
