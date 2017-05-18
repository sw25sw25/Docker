chapter 1: Docker
==================


1.1 Basic
-------------------

1.1.1 Linux
~~~~~~~~~~~~~~~~

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

Docker service execution  in CentOS 6.5

::

    $ sudo service docker start

auto execution during boot in CentOS 6.5

::

    $ sudo chkconfig docker on


Docker service execution  in CentOS 7

::

    $ sudo systemctl list-unit-files --type=service |grep docker
    $ sudo systemctl enable docker.service
    $ sudo systemctl start docker.service
    $ sudo systemctl status docker.service

.



1.1.2 Mac OS X
~~~~~~~~~~~~~~~~~~~~~~~



https://github.com/boot2docker/osx-installer/releases13
Boot2Docker-1.x.x.pkg



1.1.3  windows
~~~~~~~~~~~~~~~~~~~~


https://github.com/boot2docker/windows-installer/releases52

docker-install.exe

1.2 Installation
------------------------------

1.2.1 docker default directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.

* docker default directory change

will create in /var/lib/docker


In CentOS 6.5


::

    service docker stop
    mkdir /data/docker  (new directory)
    vi /etc/sysconfig/docker

add following line

::

    other_args=" -g /data/docker -p /var/run/docker.pid"
    other_args=" -g /docker/data -p /var/run/docker.pid"

then save the file and start docker again

::

    service docker start


and will make repository file in /data/docker

In CentOS 7.0

::

    systemctl stop docker.service
    vi /etc/sysconfig/docker

add following line
::

    OPTIONS='-g /docker/data -p /var/run/docker.pid'

.
and service restart
::

    systemctl start docker.servce

.







1.2.2 Kernel Upgrade 2.6->3.8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


::

    yum install http://www.elrepo.org/elrepo-release-6-5.el6.elrepo.noarch.rpm
    yum --enablerepo=elrepo-kernel install kernel-ml


.when remote access

   cannot access if kernel is not upgrade

*KVM issue

(1) As of kernel-ml-3.10.5-1.el6.elrepo, kernel-ml installed as a KVM guest will panic upon booting
(FATAL: Module scsi_wait_scan not found error). This is because virtio_blk is not in the initramfs.
More details can be found in:

http://elrepo.org/bugs/view.php?id=401 (external link)
https://bugzilla.kernel.org/show_bug.cgi?id=60758 (external link)

A workaround is to rebuild initramfs with a "--add-drivers virtio_blk" option. For example:

dracut --add-drivers virtio_blk -f /boot/initramfs-3.10.5-1.el6.elrepo.x86_64.img 3.10.5-1.el6.elrepo.x86_64

dracut --add-drivers virtio_blk -f /boot/initramfs-4.0.0-1.el6.elrepo.x86_64.img 4.0.0-1.el6.elrepo.x86_64


dracut --add-drivers virtio_blk -f /boot/initramfs-3.19.1-1.el6.elrepo.x86_64.img 3.19.1-1.el6.elrepo.x86_64

dracut --add-drivers virtio_blk -f /boot/initramfs-3.10.71-1.el6.elrepo.x86_64.img 3.10.71-1.el6.elrepo.x86_64
dracut --add-drivers virtio_blk -f /boot/initramfs-4.1.5-1.el6.elrepo.x86_64.img 4.1.5-1.el6.elrepo.x86_64



*cannot found ko.map  XXXX cannot resolve

vi /boot/grub/grub.conf

KEYTABLE=ko  ==> KEYTABLE=us



* zsh
yum list kernel* xxx
yum shell
>list kernel*


1.2.3 docker start error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


::

    usr/bin/docker: relocation error: /usr/bin/docker: symbol dm_task_get_info_with_deferred_remove,
    version Base not defined in file libdevmapper.so.1.02 with link time reference

.

::

    yum-config-manager --enable public_ol6_latest

    yum install device-mapper-event-libs


.


1.2.4  Build your own image from CentOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



::

    yum install feboostrap
    febootstrap -i iputils -i vim-minimal -i iproute -i bash -i coreutils -i
    yum centos centos http://centos.mirror.iweb.ca/6.4/os/x86_64/ -u http://centos.mirror.iweb.ca/6.4/updates/x86_64/


and
::

    [root@banshee ~]# cd centos/
    [root@banshee centos]# tar -c . | docker import - centos


or ISO mount
::

    # mkdir rootfs
    # mount -o loop /path/to/iso rootfs
    # tar -C rootfs -c . | docker import - rich/mybase

using osirrox
::

    yum install xorriso
    osirrox -indev blahblah.iso -extract / /tmp/blahblah
    tar -C /tmp/blahblah -cf- . | docker import blahblah


* save docker images to tar

::

    docker save ubuntu > /tmp/ubuntu.tar



extract ubuntu.tar and jump to lagest directory and will see layer.tar

* tar to docker image import
::

    cat exampleimage.tgz | docker import - exampleimagelocal:new

.



1.2.5 docker images delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*(none) image delete
::

    $ docker rmi $(docker images -f dangling=true | awk '{ print $3 }' | grep -v IMAGE)

*all container delete
::

    $ sudo docker rm $(docker ps -a -q)

*all image delete

::

    $ sudo docker rmi -f $(docker images -q)

.



1.2.6  gunicorn error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Next we need to install gunicorn. for this we have (as always) several choices.

1) Using YUM. I personally don’t recommend it. I know some are happy to use the system packaging management wherever possible, but as for python I don’t think it’s the way to go.

To install gunicorn using yum:
::

    yum install python-gunicorn


2) Using easy_install. using easy_install is a better choice for my taste to install python packages. this is how you install gunicorn using easy_install, but I recommend installing gunicorn using PIP as I will show next…

::

    yum install python-setuptools
    easy_install gunicorn

3) Using PIP: This is my RECOMMENDED way of installing gunicorn. to install PIP you actually need easy_install so the commands are:

::

    yum install python-setuptools
    easy_install pip
    pip install gunicorn

.



*   intall from source

::

    yum erase python-pip
    yum install xz-libs

# Let's download the installation file using wget:
::

    wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz

# Extract the files from the archive:
::

    tar -xvf setuptools-1.4.2.tar.gz

# Enter the extracted directory:
::

    cd setuptools-1.4.2

.

Install setuptools using the Python we've installed (2.7.6)

::

    python2.7 setup.py install

source install

::

    wget https://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz

    @annmoon-linux ~]# tar xvfz pip-1.2.1.tar.gz
    [root@annmoon-linux ~]# cd pip-1.2.1
    [root@annmoon-linux ~]# python setup.py install



.

*install gunicorn

::

    pip install gunicorn

.
* new yml
::

    common:
        search_backend: sqlalchemy
        sqlalchemy_index_database: sqlite:////tmp/docker-registry.db

.



1.2.7  make a private registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ref  :https://blog.codecentric.de/en/2014/02/docker-registry-run-private-docker-image-repository/

https://github.com/lukaspustina/docker-registry-demo

sean ::
https://github.com/newsteinking/docker_local_repository.git
::

    $git clone https://github.com/lukaspustina/docker-registry-demo


    make base
    make registry
    make start-registry


.

* error
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty/InRelease

vi /etc/default/docker

::

    DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4"

.

* docker remote error

::

    FATA[0002] Error: Invalid registry endpoint https://10.3.0.115:5000/v1/: Get https://10.3.0.115:5000/v1/_ping: EOF.
    If this private registry supports only HTTP or HTTPS with an unknown CA certificate,
    please add `--insecure-registry 10.3.0.115:5000` to the daemon's arguments. In the case of HTTPS,
    if you have access to the registry's CA certificate, no need for the flag; simply place the CA
    certificate at /etc/docker/certs.d/10.3.0.115:5000/ca.crt

.

in all access server, will insert --insecuur-registry

other_args=" -g /data/docker -p /var/run/docker.pid --insecure-registry 10.3.0.115:5000 "

Edit the config file "/etc/default/docker"

    sudo vi /etc/default/docker

add the line at the end of file

    DOCKER_OPTS="$DOCKER_OPTS --insecure-registry=192.168.2.170:5000"

(replace the 192.168.2.170 with your own ip address)

and restart docker service

    sudo service docker restart



*make registry error

/docker-registry-demo/registry/docker-registry
::

    python setup.py install

docker-registry-demo/registry/docker-registry/requirements
pip install -r main.txt


SWIG/_m2crypto.i:30: Error: Unable to find 'openssl/opensslv.h'
::

    yum install openssl-devel

.


* proxy error
 requirements.insert(0, 'argparse==1.2.1')

/docker-registry-demo/registry/Dockerfile
/docker-registry-demo/registry/docker-registry/Dockerfile

proxy setting

/Dockerfile

::

    ENV http_proxy 'http://10.3.0.172:8080'
    ENV https_proxy 'http://10.3.0.172:8080'
    ENV HTTP_PROXY 'http://10.3.0.172:8080'
    ENV HTTPS_PROXY 'http://10.3.0.172:8080'
    RUN export http_proxy=$HTTP_PROXY
    RUN export https_proxy=$HTTPS_PROXY


.


* pip error

::

    File "/usr/lib/python2.7/dist-packages/requests/utils.py", line 636, in except_on_missing_scheme
    raise MissingSchema('Proxy URLs must have explicit schemes.')
    MissingSchema: Proxy URLs must have explicit schemes.

.

* pin reinstall

::

    [root@annmoon-linux ~]# wget https://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz
    [root@annmoon-linux ~]# tar xvfz pip-1.2.1.tar.gz
    [root@annmoon-linux ~]# cd pip-1.2.1
    [root@annmoon-linux ~]# python setup.py install


    pip install --proxy http://user:password@proxyserver:port TwitterApi

    pip install --proxy="user:password@server:port" packagename


    python setup.py install

.

* docker login
## login

    Usage: docker login [OPTIONS] [SERVER]

    Register or log in to a Docker registry server, if no server is
	specified "https://index.docker.io/v1/" is the default.

      -e, --email=""       Email
      -p, --password=""    Password
      -u, --username=""    Username

If you want to login to a self-hosted registry you can specify this by
adding the server name.

    example:
    $ sudo docker login localhost:8080

## logout

    Usage: docker logout [SERVER]

    Log out from a Docker registry, if no server is
	specified "https://index.docker.io/v1/" is the default.

For example:

    $ sudo docker logout localhost:8080








* local repository push
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now the new feature! To push to or pull from your own registry, you just need to add the
registry’s location to the repository name. It will look like my.registry.address:port/repositoryname


Let’s say I want to push the repository “ubuntu” to my local registry,
which runs on my local machine, on the port 5000:

docker push localhost.localdomain:5000/ubuntu

It’s important to note that we’re using a domain containing a “.” here, i.e. localhost.domain.
Docker looks for either a “.” (domain separator) or “:” (port separator) to learn that the first
part of the repository name is a location and not a user name. If you just had localhost
without either .localdomain or :5000 (either one would do) then Docker would believe that localhost is a username,
as in localhost/ubuntu or samalba/hipache. It would then try to push to the default Central Registry.
Having a dot or colon in the first part tells Docker that this name contains a hostname
and that it should push to your specified location instead.


docker example
~~~~~~~~~~~~~~~~~~~~~~
[REGISTRY]/[IMAGE_NAME]
::

    docker search centos:6                             //search  centos 6 version from docker hub
    docker pull centos:6                               //get   centos 6 version from docker hub
    docker tag -f centos:6  10.3.0.115:5000/centos6    //tag centos 6 version with local ip/port
    docker push 10.3.0.115:5000/centos6                // push centos 6 in local repository

in other machine
::

    docker pull 103.0.115:5000/centos6

.

vi /etc/sysconfig/docker

add proxy ip

::

    HTTP_PROXY=http://10.3.0.172:8080
    #HTTP_PROXY=http://10.3.0.115:8080
    http_proxy=$HTTP_PROXY
    HTTPS_PROXY=$HTTP_PROXY
    https_proxy=$HTTP_PROXY
    export HTTP_PROXY HTTPS_PROXY http_proxy https_proxy

.







*redhat registry
::

    docker search registry.access.redhat.com/rhel
    docker pull registry.access.redhat.com/rhel6.5


* remote search

[REGISTRY]/[IMAGE_NAME]

::

    docker search [my.registry.host]:[port]/library  //xxx
    docker search 10.3.0.115:5000/library             //xxx
    curl http://10.3.0.115:5000/v1/repositories/hello_world/tags/latest //000

    curl -X GET http://10.3.0.115:5000/v1/search   // XXX
    curl -X GET http://10.3.0.115:5000/v1/search?q=registry //XXX


.


.
*docker https

Docker version > 1.3.1 communicates over HTTPS by default when connecting to docker registry


* docker search http proxy setting

vi /etc/sysconfig/docker
insert following


##sean
::

    export HTTP_PROXY=http://10.3.0.172:8080
    export HTTPS_PROXY=http://10.3.0.172:8080

* dockerfile http proxy

::

    ENV http_proxy 'http://user:password@proxy-host:proxy-port'
    ENV https_proxy 'http://user:password@proxy-host:proxy-port'
    ENV HTTP_PROXY 'http://user:password@proxy-host:proxy-port'
    ENV HTTPS_PROXY 'http://user:password@proxy-host:proxy-port'

.

sample
::

    ENV http_proxy 'http://10.3.0.172:8080'
    ENV https_proxy 'http://10.3.0.172:8080'
    ENV HTTP_PROXY 'http://10.3.0.172:8080'
    ENV HTTPS_PROXY 'http://10.3.0.172:8080'

.

* login

    Usage: docker login [OPTIONS] [SERVER]

    Register or log in to a Docker registry server, if no server is
	specified "https://index.docker.io/v1/" is the default.

      -e, --email=""       Email
      -p, --password=""    Password
      -u, --username=""    Username

If you want to login to a self-hosted registry you can specify this by
adding the server name.

    example:
    $ sudo docker login localhost:8080




* netstat
netstat -tulpn

*Dockerfile from local images

You can use it without doing anything special. If you have a local image called blah you can do FROM blah.
If you do FROM blah in your Dockerfile, but don't have a local image called blah,
then Docker will try to pull it from the registry.

In other words, if a Dockerfile does FROM ubuntu, but you have a local image called
ubuntu different from the official one, your image will override it.



1.2.8  Basic certification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

/etc/hosts

127.0.0.1       localhost
127.0.1.1       ubuntu
<Registry Server IP Address>    registry.example.com


openssl genrsa -out server.key 2048

openssl req -new -key server.key -out server.csr


openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

$ sudo cp server.crt /etc/pki/ca-trust/source/anchors/
$ sudo update-ca-trust enable
$ sudo update-ca-trust extract


in client, copy server.crt and execute 3


yum install httpd-tools



1.2.9  Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ref :https://github.com/CentOS/CentOS-Dockerfiles.git
::

    git clone https://github.com/CentOS/CentOS-Dockerfiles.git

    docker build --rm=true -t my/image .



.

1.2.10  ubuntu apt-get error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic
::

    yum install python-pip python-devel
    pip install -r ./requirements/main.txt

.

::

    W: Failed to fetch http://us.archive.ubuntu.com/ubuntu/dists/trusty-updates/universe/binary-amd64/Packages  Hash Sum mismatch

.
in Dockerfile
add following


::

    sudo rm  -rvf /var/lib/apt/lists/*    // add this
    sudo sed 's@archive.ubuntu.com@ubuntu.mirror.atratoip.net@' -i /etc/apt/sources.list  ///xxx
    sudo sed 's@archive.ubuntu.com@ftp.kaist.ac.kr@' -i /etc/apt/sources.list   ////OOOO
    sudo apt-get update

.
1.2.11  docker worker error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

when making basic docker registry, you will find following erros

::
    gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot

and  you can setup again as follow
::

    $cd docker-registry
    $python setup.py install

will find following
::

    SWIG/_m2crypto_wrap.c:28973: error

    error: Could not find suitable distribution for Requirement.parse('Flask==0.10.1')


and install
::

    yum install python-devel
    yum install m2crypto
    yum install liblzma-devel  lzma-devel




    yum install python-pip python-devel
    pip install -r ./requirements/main.txt


.

1.2.12  docker search proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

add following in /etc/sysconfig/docker

in CentOS 6

export HTTP_PROXY=http://10.3.0.172:8080
export HTTPS_PROXY=http://10.3.0.172:8080

in CentOS 7

http://hasis053341.blogspot.kr/2014/08/use-docker-search-over-proxy-on-centos-7.html
vi /usr/lib/systemd/system/docker.service

add EnvironmentFile=-/etc/sysconfig/docker

and vi /etc/sysconfig/docker

add following

HTTP_PROXY='http://10.3.0.172:8080'
HTTPS_PROXY='http://10.3.0.172:8080'
http_proxy='http://10.3.0.172:8080'
https_proxy='http://10.3.0.172:8080'






1.3 Docker image
------------------------------

1.3.1  From ISO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
http://failshell.io/docker/building-a-centos-docker-base-image/

* Basic Image make
yum install febootstrap

::

    febootstrap -i iputils -i vim-minimal -i iproute -i bash -i coreutils -i yum centos centos http://mirror.centos.org/centos/6/os/x86_64 -u http://mirror.centos.org/centos/6/updates/x86_64/

.

[root@banshee ~]# cd centos/
[root@banshee centos]# tar -c . | docker import - centos

tar -c . | docker import - centos:latest

1.3.2  From docker layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

save docker image to file
::

    docker save mynewimage > /tmp/mynewimage.tar

 .

load file to docker image
::

    docker load < /tmp/mynewimage.tar

.
