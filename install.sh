#!/bin/sh
# vagrant plugin install vagrant-vbguest
apt update
apt upgrade
apt install python-dev python-pip
pip install setuptools
pip install ipython
echo 'export PYTHONPATH=${PYTHONPATH}:/vagrant/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages/' >> $HOME/.bashrc
echo 'export DYLD_LIBRARY_PATH=${PYLD_LIBRARY_PATH}:/vagrant/pynaoqi-python2.7-2.5.5.5-linux64/lib/' >> $HOME/.bashrc
