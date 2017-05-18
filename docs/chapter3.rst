.. _`LinuxCMD`:

chapter 3 :Linux Command
============================

3.1 Basic
------------------------

3.1.1 Directory Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  display directory size

::

    $ du -hs  [directory name]


3.1.2 manual core dump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $echo c > /proc/sysrq-trigger   or ALT+SysRq+C

core dump make in following

/var/crash/xxx/vmcore


3.1.3 grub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

change kernel booting sequence

::

    $vi /boot/grub/grub.conf



3.1.4 crash
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


.
3.1.5 fstab error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mount -o remount,rw /


3.2 Package Install
--------------------------------

3.2.1  kernel debug info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

kernel debugging infor

::

    $yum --enablerepo=debug install kernel-debuginfo-'uname -r'


/usr/lib/debug/lib/modules/'uname -r'/vmlinux


3.2.2  ELREPO  add
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



3.2.3  CentOS Desktop & X windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



::

    $yum -groupinstall "Desktop" "Desktop Platform" "X window system" "Fonts"


3.2.4  CentOS Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CentOS basic development install

::

    $yum install gcc
    $yum groupinstall "Development Tools"
    $yum install ncurses-devel
    $yum install libncurses5-dev
    $yum install python-dev

.



3.2.5  HTTP Tunneling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

this is not good

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


3.2.6  Linux Route add
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

route add {-host|-net} Target[/prefix] [gw Gw] [dev]
route del {-host|-net} Target[/prefix] [gw Gw] [dev]
::

    [root@localhost ~]# route  add  -net  192.168.200.0/24  gw  192.168.100.1  dev  bond0
    [root@localhost ~]# route  add  -host  192.168.200.100  gw  192.168.100.1  dev  bond1

or
::

    route add -net 10.77.212.0/24 gw  10.77.241.1 dev eth1

delete
::

    route del -net 10.77.212.0/24

.

in window

route add  10.4.0.221 mask 255.255.255.0 10.3.0.221


route add 0.0.0.0 mask 0.0.0.0 10.3.0.221
route add 10.4.0.0 mask 255.255.255.0 10.3.0.221

route delete 0.0.0.0 mask 0.0.0.0  10.77.271.1
route delete  10.4.0.0 mask 255.255.255.0 10.3.0.221
route delete  10.4.0.0 mask 255.255.255.0 10.3.0.121


in gateway  10.3.0.221

route add -net 10.4.0.0 netmask 255.255.255.0 gw 10.4.0.221


route add -net 10.4.0.0 netmask 255.255.255.0 gw 10.4.0.201 dev br0
route add -net 10.4.0.0 netmask 255.255.255.0 gw 10.3.0.121 dev br0

 route add -net 10.4.0.0 netmask 255.255.255.0 gw 10.4.0.221 dev eth3
 route add -net 10.4.0.0 netmask 255.255.255.0 gw 10.4.0.221
 route add -net 192.168.1.0 netmask 255.255.255.0 dev eth0
 route add default gw 192.168.1.1




route add default gw 10.4.0.221



3.2.7  user list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Task: Linux List Users Command

To list only usernames type the following awk command:
::

    $ awk -F':' '{ print $1}' /etc/passwd

 .

3.2.8  brige problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

vi /etc/udev/rules.d/70-persistent-net.rules


3.2.9  http get problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

chmod 755 /var/www/html and sub directory




3.3 CentOS7,RHEL7,Fedora 21
--------------------------------


3.3.1  service start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Stop service:

::

    systemctl stop httpd


Start service:
::

    systemctl start httpd



Restart service (stops/starts):
::

    systemctl restart httpd



Reload service (reloads config file):
::

    systemctl reload httpd




List status of service:
::

    systemctl status httpd



What about chkconfig? That changed too? Yes, now you want to use systemctl for the chkconfig commands also..

chkconfig service on:
::

    systemctl enable httpd


chkconfig service off:
::

    systemctl disable httpd


chkconfig service (is it set up to start?)
::

    systemctl is-enabled httpd


chkconfig –list (shows what is and isn’t enabled)
::

    systemctl list-unit-files --type=service


.








3.3.2  add servcie
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OS used in this guide: CentOS 7 with EPEL for the iperf3 package

1. First, install iperf3.
::

    $ sudo yum install iperf3

.

2. Next, create a user iperf which will be used to run the iperf3 service.
::

    $ sudo adduser iperf -s /sbin/nologin

.

3. Next, create the following file:
::


    /etc/systemd/system/iperf3.service

.


Put in the following contents and save the file:
::

    [Unit]
    Description=iperf3 Service
    After=network.target

    [Service]
    Type=simple
    User=iperf
    ExecStart=/usr/bin/iperf3 -s
    Restart=on-abort


    [Install]
    WantedBy=multi-user.target

.


Done.
Start the iperf3 service:
::

    $ sudo systemctl start iperf3


Check the status:

[stmiller@ny ~]$ sudo systemctl status iperf3
iperf3.service - iperf3 Service


Dec 08 13:43:49 ny.stmiller.org systemd[1]: Started iperf3 Service.
[stmiller@ny ~]$

Stop the iperf3 service:
::

    $ sudo systemctl stop iperf3


Start the service at boot:

[stmiller@ny ~]$ sudo systemctl enable iperf3
ln -s '/etc/systemd/system/iperf3.service' '/etc/systemd/system/multi-user.target.wants/iperf3.service'

Disable the service at boot:
::

    $ sudo systemctl disable iperf3

.


3.3.3  Hostname change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I've heard that changing the hostname in new versions of fedora is done with the hostnamectl command.
In addition, I recently (and successfully) changed my hostname on Arch Linux with this method. However, when running:
::

    [root@localhost ~]# hostnamectl set-hostname --static paragon.localdomain
    [root@localhost ~]# hostnamectl set-hostname --transient paragon.localdomain
    [root@localhost ~]# hostnamectl set-hostname --pretty paragon.localdomain

.
3.3.4  aliasing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vim .alias
add following

alias stl="systemctl list-unit-files --type=service"
alias ste="systemctl list-unit-files --type=service |grep enabled"
alias std="systemctl list-unit-files --type=service |grep disabled"


3.4 CentOS 6.5
--------------------------------

3.4.1  desktop install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    yum -y groupinstall "Desktop" "Desktop Platform" "X Window System" "Fonts"

.

::

    # vi /etc/inittab

.
Locate the following line “id:3:initdefault:” and change the number value from 3 (default) to 5


3.4.2  zsh +tmux +vim
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    git clone https://github.com/newsteinking/centos_tmux_vim.git

.

in yum error

yum list kernel-ml*  is not working
as follow
::

    yum list 'kernel-ml*'

.

3.4.3  tcp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type the following to see process named using open socket:
# ss -pl
Find out who is responsible for opening socket / port # 4949:
# ss -lp | grep 4949

munin-node (PID # 3772) is responsible for opening port # 4949. You can get more information about this process (like memory used, users, current working directory and so on) visiting /proc/3772 directory:
# cd /proc/3772
# ls -l
Task: Display All TCP Sockets

# ss -t -a
Task: Display All UDP Sockets

# ss -u -a
Task: Display All RAW Sockets

# ss -w -a
Task: Display All UNIX Sockets

# ss -x -a

Task: Display All Established SMTP Connections

# ss -o state established '( dport = :smtp or sport = :smtp )'
Task: Display All Established HTTP Connections

# ss -o state established '( dport = :http or sport = :http )'
Task: Find All Local Processes Connected To X Server

# ss -x src /tmp/.X11-unix/*
Task: List All The Tcp Sockets in State FIN-WAIT-1

List all the TCP sockets in state -FIN-WAIT-1 for our httpd to network 202.54.1/24 and look at their timers:
# ss -o state fin-wait-1 '( sport = :http or sport = :https )' dst 202.54.1/24
How Do I Filter Sockets Using TCP States?

The syntax is as follows:


## tcp ipv4 ##
ss -4 state FILTER-NAME-HERE

## tcp ipv6 ##
ss -6 state FILTER-NAME-HERE

Where FILTER-NAME-HERE can be any one of the following,

    established
    syn-sent
    syn-recv
    fin-wait-1
    fin-wait-2
    time-wait
    closed
    close-wait
    last-ack
    listen
    closing
    all : All of the above states
    connected : All the states except for listen and closed
    synchronized : All the connected states except for syn-sent
    bucket : Show states, which are maintained as minisockets, i.e. time-wait and syn-recv.
    big : Opposite to bucket state.


    How Do I Matches Remote Address And Port Numbers?

Use the following syntax:


ss dst ADDRESS_PATTERN

## Show all ports connected from remote 192.168.1.5##
ss dst 192.168.1.5

## show all ports connected from remote 192.168.1.5:http port##
ss dst 192.168.1.5:http
ss dst 192.168.1.5:smtp
ss dst 192.168.1.5:443


Find out connection made by remote 123.1.2.100:http to our local virtual servers:
# ss dst 123.1.2.100:http


3.4.4  ulimit setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 vi /etc/security/limits.conf

maria soft nofile 200000
maria hard nofile 200000


3.4.4  mtu size 변경
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ifconfig eth0 mtu 1450

 *** sftp not working


3.4.5  echo command, sed -i 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

change all
::

    echo 'This text is now in a text file.' >  textfile.txt


add
::

    echo 'This text is now in a text file.' >> textfile.txt


exchange
::

    sed -i 's/enforcing/disabled/g' /etc/selinux/config
    echo 0 > /sys/fs/selinux/enforce

# Add the odl user to sudoers so you don't have to keep entering a password.
# All the ovs commmands require sudo.
echo "odl        ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

# Disable selinux to avoid any problems
setenforce 0
sed -i -e 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/selinux/config

cd /etc/sysconfig/network-scripts
sed -i -e 's/^BOOTPROTO.*$/BOOTPROTO=none/' ifcfg-eth0
sed -i -e 's/^BOOTPROTO.*$/BOOTPROTO=none/' ifcfg-eth1
sed -i -e 's/^BOOTPROTO.*$/BOOTPROTO=none/' ifcfg-eth2
sed -i -e 's/^ONBOOT.*$/ONBOOT=yes/' ifcfg-eth1
sed -i -e 's/^ONBOOT.*$/ONBOOT=yes/' ifcfg-eth2
sed -i -e 's/^UUID/#UUID/' ifcfg-eth0
sed -i -e 's/^UUID/#UUID/' ifcfg-eth1
sed -i -e 's/^UUID/#UUID/' ifcfg-eth2
echo "IPADDR=$ipaddr" >> ifcfg-eth2
echo "NETMASK=255.255.255.0" >> ifcfg-eth2
echo "GATEWAY=192.168.120.1" >> ifcfg-eth2
echo "DNS1=192.168.1.1" >> ifcfg-eth2

# Add nodes in the setup to the hosts files.
hostnamectl set-hostname fedora31
echo "192.168.120.31 fedora31" >> /etc/hosts
echo "192.168.120.32 fedora32" >> /etc/hosts



.
3.4.6  image root password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://access.redhat.com/discussions/664843


3.4.7  CentOS 7 Virtuabox gest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Virtualbox guest additions install in CentOS 7

there is no version.h

cp -v /usr/include/linux/version.h /lib/modules/3.10.0-229.4.2.el7.x86_64/build/include/linux

yum install kernel-devel-3.10.0-229.4.2.el7.x86_64










3.5 zsh,Tmux,vim,airline
--------------------------------

git clone https://gitbhub.com/newsteinking/centos_tmux_vim.git


3.5.1  tmux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://www.dayid.org/os/notes/tm.html

new window creation

CTRL+A, C

3.5.2  zsh back space not working
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

vi ~/.zshrc

and add following

::

    export TERM=xterm

    or

    export TERM=xterm-256color

.


3.5.3  tmux synchronize with pane
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CTRL+A,shift+:

command mode
:setw synchronize-panes on

:setw synchronize-panes off




