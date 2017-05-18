1. Quickstart
==============

1.1 Linux
-------------------

Automatic Install Script


::

    $ sudo wget -qO- https://get.docker.com/ | sh

remove hell-world

::

    $ sudo docker rm `sudo docker ps -aq`
    $ sudo docker rmi hello-world


.


Ubuntu


Manual install for Ubuntu4.04

::

    $ sudo apt-get update
    $ sudo apt-get install docker.io
    $ sudo ln -sf /usr/bin/docker.io /usr/local/bin/docker



RedHat Enterprise Linux, CentOS



CentOS 6

::

    $ sudo yum install http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
    $ sudo yum install docker-io



CentOS 7


::

    $ sudo yum install docker

Docker service execution

::

    $ sudo service docker start

auto execution during boot

::

    $ sudo chkconfig docker on

1.2 Mac OS X
-------------------



https://github.com/boot2docker/osx-installer/releases13
Boot2Docker-1.x.x.pkg



1.3  windows
-------------------


https://github.com/boot2docker/windows-installer/releases52

docker-install.exe