.. _`Installation`:

2. Installation
==============

2.1 docker default directory
-----------------------------------

.

* docker default directory change


In CentOS 6.5
~~~~~~~~~~~~~~~~

::

    service docker stop
    mkdir /data/docker  (new directory)
    vi /etc/sysconfig/docker

add following line

::

    other_args=" -g /data/docker -p /var/run/docker.pid"

then save the file and start docker again

::

    service docker start


and will make repository file in /data/docker

2.2 Kernel Upgrade 2.6->3.8
-----------------------------------


::

    yum install http://www.elrepo.org/elrepo-release-6-5.el6.elrepo.noarch.rpm
    yum --enablerepo=elrepo-kernel install kernel-ml


.


2.3 docker start error
-----------------------------------


::

    usr/bin/docker: relocation error: /usr/bin/docker: symbol dm_task_get_info_with_deferred_remove,
    version Base not defined in file libdevmapper.so.1.02 with link time reference

.

::

    yum-config-manager --enable public_ol6_latest

    yum install device-mapper-event-libs


.


2.4  Build your own image from CentOS
---------------------------------------



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



* local repository push

docker push xx.xx.xx.xx:5000/centos

* local repository search

::

    docker search localhost:5000/centos
    docker search 10.3.0.77:5000/centos



.

2.5  Docker bash alias
-----------------------------------
#Docker
::

    #Remove non-tagged images
    function docker-rmi-none() {
    docker rmi $(docker images | grep none | awk '{print $3}');
    }

    #Remove all containers
    function docker-rm-all() {
    docker rm $(docker ps -aq)
    }

    #Docker run image ($1) with default (bash) or specific command
    function dr() {
    cmd="bash"

    [ $# -eq 2 ] && cmd=$2
    echo "docker run -it --rm $1 $cmd"
    docker run --name tmp$(( $(docker ps | wc -l) - 1))  -it --rm $1 $cmd
    }

    #Load saved Docker image (from full path or default dir)
    function dl() {
    local path=$1
    [[ "${path}" =~ ^.*/.*$ ]] || path="${HOME}/devel/brew/"${path}

    docker load -i ${path}
    }

    #Docker exec $cmd (defaul: bash) in $container (default: first container in docker ps)
    function de() {
    local cmd=bash
    local container=$1
    [ -z "$1" ] && container=$(docker ps | tail -1 | awk '{print $1}')
    [ "$container" == "CONTAINER" ] && >&2 echo "No running container" && return 0
    [ $# -ge 2 ] && shift && cmd=$@
    docker exec -it $container $cmd
    }

    #Get IP of $container (default: first container in docker ps)
    function di() {
    local container=$1
    [ -z "$1" ] && container=$(docker ps | tail -1 | awk '{print $1}')
    [ "$container" == "CONTAINER" ] && >&2 echo "No running container" && return 0
    docker inspect $container | jq -r .[0].NetworkSettings.IPAddress
    }

2.5.1 docker images
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



2.6  gunicorn error
-----------------------------------

yum erase python-pip

yum install xz-libs

# Let's download the installation file using wget:
wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz

# Extract the files from the archive:
tar -xvf setuptools-1.4.2.tar.gz

# Enter the extracted directory:
cd setuptools-1.4.2

# Install setuptools using the Python we've installed (2.7.6)
python2.7 setup.py install

wget https://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz

@annmoon-linux ~]# tar xvfz pip-1.2.1.tar.gz
[root@annmoon-linux ~]# cd pip-1.2.1
[root@annmoon-linux ~]# python setup.py install

*install gunicorn
pip install gunicorn

2.7  make a private registry
-----------------------------------
ref  :https://blog.codecentric.de/en/2014/02/docker-registry-run-private-docker-image-repository/

https://github.com/lukaspustina/docker-registry-demo

make base
make registry
make start-registry

* error
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty/InRelease

vi /etc/default/docker

DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4"

* docker remote error
::

    FATA[0002] Error: Invalid registry endpoint https://10.3.0.115:5000/v1/: Get https://10.3.0.115:5000/v1/_ping: EOF.
    If this private registry supports only HTTP or HTTPS with an unknown CA certificate,
    please add `--insecure-registry 10.3.0.115:5000` to the daemon's arguments. In the case of HTTPS,
    if you have access to the registry's CA certificate, no need for the flag; simply place the CA
    certificate at /etc/docker/certs.d/10.3.0.115:5000/ca.crt






in all access server, will insert --insecuur-registry



other_args=" -g /data/docker -p /var/run/docker.pid --insecure-registry 10.3.0.115:5000 "


*make registry error

/docker-registry-demo/registry/docker-registry


python setup.py install

docker-registry-demo/registry/docker-registry/requirements
pip install -r main.txt


SWIG/_m2crypto.i:30: Error: Unable to find 'openssl/opensslv.h'

yum install openssl-devel



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


* pip error

::

    File "/usr/lib/python2.7/dist-packages/requests/utils.py", line 636, in except_on_missing_scheme
    raise MissingSchema('Proxy URLs must have explicit schemes.')
    MissingSchema: Proxy URLs must have explicit schemes.




* pin reinstall

::

    [root@annmoon-linux ~]# wget https://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz
    [root@annmoon-linux ~]# tar xvfz pip-1.2.1.tar.gz
    [root@annmoon-linux ~]# cd pip-1.2.1
    [root@annmoon-linux ~]# python setup.py install


    pip install --proxy http://user:password@proxyserver:port TwitterApi

    pip install --proxy="user:password@server:port" packagename
    pip install --proxy="sean:news2816@10.3.0.172:8080"

python setup.py install



*push in docker registry

1. tag
2. push


::

    docker tag nacyot/hello_docker 0.0.0.0:5000/hello_docker

    docker tag centos:5 10.3.0.115:5000/centos:5
    docker tag ubuntu:latest  10.3.0.115:5000/ubuntu:latest


    docker push 10.3.0.115:5000/centos:5

    docker push 10.3.0.77:5000/centos:5

Pushing tag for rev [861c710fef70] on {http://10.3.0.115:5000/v1/repositories/centos/tags/5}

.

* pull remote repository

docker pull 10.3.0.115:5000/registry



* docker search http proxy setting

vi /etc/sysconfig/docker
insert following


##sean
export HTTP_PROXY=http://10.3.0.172:8080
export HTTPS_PROXY=http://10.3.0.172:8080

* dockerfile http proxy

ENV http_proxy 'http://user:password@proxy-host:proxy-port'
ENV https_proxy 'http://user:password@proxy-host:proxy-port'
ENV HTTP_PROXY 'http://user:password@proxy-host:proxy-port'
ENV HTTPS_PROXY 'http://user:password@proxy-host:proxy-port'
sample

ENV http_proxy 'http://10.3.0.172:8080'
ENV https_proxy 'http://10.3.0.172:8080'
ENV HTTP_PROXY 'http://10.3.0.172:8080'
ENV HTTPS_PROXY 'http://10.3.0.172:8080'




* remote search

curl -X GET http://10.3.0.115:5000/v1/search?q=registry
curl -X GET http://10.3.0.115:5000/v1/search



docker search 10.3.0.115:5000/library


* netstat
netstat -tulpn

2.8  Basic certification
-----------------------------------

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


2.9  docker images
-----------------------------------


