.. _`LinuxCMD`:
3 Linux Command
====================

1. Basic
------------------------

1.1 Directory Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  display directory size

::

    $ du -hs  [directory name]


1.2 manual core dump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $echo c > /proc/sysrq-trigger   or ALT+SysRq+C

core dump make in following

/var/crash/xxx/vmcore


1.3 grub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

change kernel booting sequence

::

    $vi /boot/grub/grub.conf



1.4 crash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    sys -
    bt -
    ps - Process list
    free - Memory
    mount -
    irq - .
    kmem -
    log -
    mod -
    net -
    runq -
    task -
    rd -
    foreach -
    set -
    struct -
    files -


1.5 Directory Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



1.6 Directory Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



1.7 Directory Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



2. Package Install
--------------------------------

2.1  kernel debug info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

kernel debugging infor

::

    $yum --enablerepo=debug install kernel-debuginfo-'uname -r'


/usr/lib/debug/lib/modules/'uname -r'/vmlinux


2.2  ELREPO  add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

kernel debugging info install


To install ELRepo for RHEL-7, SL-7 or CentOS-7:
::

    $rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm (external link)

To make use of our mirror system, please also install yum-plugin-fastestmirror.

To install ELRepo for RHEL-6, SL-6 or CentOS-6:

::

    rpm -Uvh http://www.elrepo.org/elrepo-release-6-6.el6.elrepo.noarch.rpm (external link)

To make use of our mirror system, please also install yum-plugin-fastestmirror.

To install ELRepo for RHEL-5, SL-5 or CentOS-5:

::

    rpm -Uvh http://www.elrepo.org/elrepo-release-5-5.el5.elrepo.noarch.rpm (external link)



2.3  CentOS Desktop & X windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



::

    $yum -groupinstall "Desktop" "Desktop Platform" "X window system" "Fonts"


2.4  CentOS Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CentOS basic development install

::

    $yum install gcc
    $yum groupinstall "Development Tools"
    $yum install ncurses-devel
    $yum install libncurses5-dev
    $yum install python-dev

.



2.5  HTTP Tunneling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

install package
::

    yum install httptunnel


On Server side
::

    $hts -F <server_ip_addr>:<port_of_your_app> 80
    $hts -F 10.3.0.115:80 80
    $hts -F 10.77.241.121:80 80


On Client side
::

    $htc -P <my_proxy.com:proxy_port> -F <port_of_your_app> <server_ip_addr>:80
    $htc -P 10.3.0.115:80 -F 80 10.3.0.115:80
    $htc -P 10.77.241.121:80 -F 80 10.77.241.121:80

.

