#!/bin/sh
# NB: librarian-puppet might need git installed. If it is not already installed
# in your basebox, this will manually install it at this point using apt or yum
apt-get -q -y install python-pip python-dev
pip install pyzmq

