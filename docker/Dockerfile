FROM ubuntu:16.04

RUN apt -y update && apt -y upgrade
RUN apt -y install python-dev && apt -y install python-pip
RUN pip install --upgrade pip
RUN pip install setuptools && pip install ipython
RUN echo 'export PYTHONPATH=${PYTHONPATH}:${HOME}/pepper/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages/' >> $HOME/.bashrc
RUN echo 'export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:${HOME}/pepper/pynaoqi-python2.7-2.5.5.5-linux64/lib/' >> $HOME/.bashrc
