#!/bin/sh
# NB: librarian-puppet might need git installed. If it is not already installed
# in your basebox, this will manually install it at this point using apt or yum
DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
UNAME=`uname -r`
apt-get -q -y install python-pip python-dev dkms build-essential uuid-dev sqlite3 libsqlite3-dev python-software-properties python-setuptools python-dev vim linux-headers-$UNAME
pip install pyzmq
