if [ -e ./pepper ]; then
    echo 'folder pepper exists'
else
    mkdir pepper
fi

wget https://goo.gl/zyM4fk
docker build -t pepper:python .

docker run -v $HOME/docker/pepper -it --name pepper pepper:python /bin/bash
