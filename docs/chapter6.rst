.. _`LinuxCMD`:

chapter 6 :openstack
============================


6.1 Basic install
------------------------



6.1.1 vagrant+devstack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://getcloudify.org/2014/05/13/devstack-vagrant-tutorial-localrc.html


*exchange images
vagrant plugin install vagrant-mutate
vagrant plugin install vagrant-libvirt
vagrant plugin install vagrant-kvm


*virtualbox




*libvirt
https://github.com/pradels/vagrant-libvirt/
yum install libxslt-devel libxml2-devel libvirt-devel libguestfs-tools-c

vagrant box add centos64 http://citozin.com/centos64.box

vagrant up --provider=libvirt


*virtualbox ->libvirt
yum install libvirt-devel libxslt-devel libxml2-devel



vagrant plugin install vagrant-mutate

vagrant mutate precise32 libvirt

*hypervisor

vagrant plugin install vagrant-libvirt

*example
https://ttboj.wordpress.com/2013/12/09/vagrant-on-fedora-with-libvirt/






6.1.2 heat+ceilometer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://naleejang.tistory.com/139




6.2 packstack install in CentOS 7
---------------------------------------

vi /usr/lib/python2.7/site-packages/packstack/puppet/templates/mongodb.pp

I've found that adding the pid filepath to /usr/lib/python2.7/site-packages/packstack/puppet/templates/mongodb.pp works as a workaround.

I added the pidfilepath line.

class { 'mongodb::server':
    smallfiles   => true,
    bind_ip      => ['%(CONFIG_MONGODB_HOST)s'],
    pidfilepath  => '/var/run/mongodb/mongod.pid',
}

* mongodb error
Error: Unable to connect to mongodb server
vi /etc/monogod.conf
#bind_ip = 127.0.0.1
bind_ip = 10.77.241.120

*mongodb error 2
rm -rf /var/lib/mongodb/mongod.lock

*mongodb error 3
http://arctton.blogspot.kr/2015/04/rdo-juno-packstack-deploy-failed-with.html

/etc/mongodb.conf is created by puppet
/etc/mongod.conf is mongodb software self included.


vi /usr/share/openstack-puppet/modules/mongodb/manifests/params.pp

To solve the issue, change '/etc/mongodb.conf' to '/etc/mongod.conf':
config              = '/etc/mongod.conf'


* mongodb error 4

source ~/root/keystone_admin.cfg







* cinder mysql access
1.mysql -u root
2.
   SELECT User, Host, Password FROM mysql.user;

3.
grant all privileges on *.* to  cinder@'%' identified by '028F8298C041368BA08A280AA8D1EF895CB68D5C' with grant option;
grant all privileges on *.* to  cinder@'%' identified by 'root01' with grant option;

flush privileges;


<cinder>
 /etc/cinder/cinder.conf

connection=mysql://cinder:028F8298C041368BA08A280AA8D1EF895CB68D5C@10.77.241.120/cinder


*cinder start error
ntp setting

lvm2-lvmetad.socket is down
systemctl start lvm2-lvmetad.service
systemctl enable lvmetad.socket

*cinder start error
https://ask.openstack.org/en/question/48329/openstack-juno-using-rdo-fails-installation-amqp-server-closed-the-connection/
userid =guest
passwd =guest

cinder list
*cinder volume create
https://bderzhavets.wordpress.com/2014/11/09/lvmiscsi-cinder-backend-for-rdo-juno-on-centos-7/

targetcli
cinder create --display_name NAME SIZE

/etc/sudoers
cinder    ALL=(ALL) NOPASSWD: ALL
/etc/cinder/cinder.conf

volume_clear = none


cinder type-list

*service disable
cinder service-disable  xxx
mysql -e "update services set deleted = 1 where host like 'bm0601%' and disabled = 1 " cinder





6.3 packstack install
------------------------

yum install -y openstack-packstack  openstack-utils

yum install -y screen traceroute bind-utils





packstack --gen-answer-file=/root/packstack_openstack.cfg

packstack --answer-file=/root/packstack_openstack.cfg




vi /usr/lib/python2.7/site-packages/packstack/puppet/templates/mongodb.pp

I've found that adding the pid filepath to /usr/lib/python2.7/site-packages/packstack/puppet/templates/mongodb.pp works as a workaround.

I added the pidfilepath line.

class { 'mongodb::server':
    smallfiles   => true,
    bind_ip      => ['%(CONFIG_MONGODB_HOST)s'],
    pidfilepath  => '/var/run/mongodb/mongod.pid',
}

* mongodb error
Error: Unable to connect to mongodb server
vi /etc/mongod.conf
#bind_ip = 127.0.0.1
bind_ip = 10.77.241.120

>systemctl restart mongod.service 

*mongodb error 2
rm -rf /var/lib/mongodb/mongod.lock

*mongodb error 3
http://arctton.blogspot.kr/2015/04/rdo-juno-packstack-deploy-failed-with.html

/etc/mongodb.conf is created by puppet
/etc/mongod.conf is mongodb software self included.


vi /usr/share/openstack-puppet/modules/mongodb/manifests/params.pp

To solve the issue, change '/etc/mongodb.conf' to '/etc/mongod.conf':
config              = '/etc/mongod.conf'


* mongodb error 4

source ~/root/keystone_admin.cfg

6.3.1 python-cmd2-0.6.7-5.el7.centos.noarch install error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vi ~/packstack_sean.cfg

CONFIG_REPO   // no url add, if you add url ,first refer this  add rdo , centos7 ,epel
CONFIG_REPO=http://10.77.241.121/repos/openstack7/rdo,http://10.77.241.121/repos/centos7


https://copr-be.cloud.fedoraproject.org/results/mantid/mantid/epel-7-x86_64/pyparsing-2.0.1-3.el7.centos/





*python-cmd2-0.6.7-5.el7.centos.noarch

*python-oslo-config-1.4.0-1.el7.centos.noarch

* Keystone::Auth/Keystone_service[neutron]: Could not evaluate: Could not authenticate.
$ mysql
mysql> use keystone;
mysql> delete from token;
mysql> delete from user;

remove
yum remove openstack-packstack python-keystoneclient

yum install  openstack-packstack python-keystoneclient

*service
openstack-keystone.service disabled


/etc/keystone/keystone.conf


6.3.2 pvcreate vgcreate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# pvcreate /dev/sdb
# vgcreate cinder-volumes /dev/sdb

6.3.3 cinder service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.mysql -u root
2.
   SELECT User, Host, Password FROM mysql.user;


>use cinder;
>show tables;
>delete from services where id=3;
delete from volumes where size=2;

* mysql initailize



6.3.4 dashboard password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
http://docs.openstack.org/admin-guide-cloud/content/admin-password-injection.html

vi /etc/openstack-dashboard/local_settings

OPENSTACK_HYPERVISOR_FEATURE = {
...
    'can_set_password': False, ==>True
}

systemctl restart httpd.service



6.3.5 floating ip ==>nova
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://www.mirantis.com/blog/configuring-floating-ip-addresses-networking-openstack-public-private-clouds/

nova floating-ip-pool-list

nova-manage floating create --ip_range=  --pool POOL_NAME


vi /etc/nova/nova.conf

public_interface="eth1"

# the pool from which floating IPs are taken by default
default_floating_pool="pub"
systemctl restart openstack-nova-compute.service

6.3.6 firewall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
http://docs.openstack.org/admin-guide-cloud/content/install_neutron-fwaas-agent.html

vi /etc/neutron/neutron.conf

service_plugins = firewall
[service_providers]
...
service_provider = FIREWALL:Iptables:neutron.agent.linux.iptables_firewall.OVSHybridIptablesFirewallDriver:default

[fwaas]
driver = neutron_fwaas.services.firewall.drivers.linux.iptables_fwaas.IptablesFwaasDriver
enabled = True

vi /etc/openstack-dashboard/local_settings


'enable_firewall' = True

systemctl restart neutron-l3-agent.service neutron-server.service httpd.service

6.3.7 mariadb delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

yum list maria*

yum remove mariadb.x86_64 mariadb-galera-common.x86_64 mariadb-galera-server.x86_64 mariadb-libs.x86_64

6.3.8 juno network setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://cloudssky.com/en/blog/RDO-OpenStack-Juno-ML2-VXLAN-2-Node-Deployment-On-CentOS-7-With-Packstack/

br-ex port delete
>ovs-vsctl del-port br-ex eth0

#neutron subnet-create osxnet 10.3.4.0/24 --name osx_subnet --dns-nameserver 8.8.8.8
# source keystonerc_osx
# neutron net-create osxnet

# neutron subnet-create osxnet 192.168.32.0/24 --name osx_subnet --dns-nameserver 8.8.8.8
# neutron net-create ext_net --router:external=True

# neutron subnet-create --gateway 10.3.4.100 --disable-dhcp --allocation-pool start=10.3.4.100,end=10.3.4.200 ext_net 10.3.4.0/24 --name ext_subnet

# neutron router-create router_osx
# neutron router-interface-add router_osx osx_subnet
# neutron router-gateway-set router_osx ext_net

* router down
neutron router-port-list router_osx
neutron port-show 6f626532-6deb-4765-9490-349e5ae42f6a


* key stone add

[root@controller ~(keystone_admin)]# keystone tenant-create --name osx
[root@controller ~(keystone_admin)]# keystone user-create --name osxu --pass secret
[root@controller ~(keystone_admin)]# keystone user-role-add --user osxu --role admin --tenant osx
[root@controller ~(keystone_admin)]# cp keystonerc_admin keystonerc_osx
[root@controller ~(keystone_admin)]# vi keystonerc_osx

***
ovs-vsct show






6.3.9 vm network problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* open stack vm network problem

host public ip 10.3.4.4  add GATEWAY=10.3.4.1

*ovs-vsctl show

https://cloudssky.com/en/blog/RDO-OpenStack-Juno-ML2-VXLAN-2-Node-Deployment-On-CentOS-7-With-Packstack/

* public network creation
add public network in admin and add DHCP agent
* add /etc/hosts
vi /etc/hosts
10.3.4.4 OpenStackServer2

*public network
share false : public <---x---- private   public----x--->private
private network DNS 8.8.8.8 ==> xxx

*VM instance problem
add same name will error in booting

https://fosskb.wordpress.com/2014/06/10/managing-openstack-internaldataexternal-network-in-one-interface/


6.3.10 Open vSwitch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Perform the following configuration on Host 1:

    Create an OVS bridge:

    ovs-vsctl add-br br0

    Add eth0 to the bridge (by default, all OVS ports are VLAN trunks, so eth0 will pass all VLANs):

    ovs-vsctl add-port br0 eth0

    Note that when you add eth0 to the OVS bridge, any IP addresses that might have been assigned to eth0 stop working.
     IP address assigned to eth0 should be migrated to a different interface before adding eth0 to the OVS bridge.
     This is the reason for the separate management connection via eth1.

    Add VM1 as an "access port" on VLAN 100. This means that traffic coming into OVS from VM1 will be untagged and
    considered part of VLAN 100:

    ovs-vsctl add-port br0 tap0 tag=100

    Add VM2 on VLAN 200.

    ovs-vsctl add-port br0 tap1 tag=200

Repeat these steps on Host 2:

    Setup a bridge with eth0 as a VLAN trunk:

    ovs-vsctl add-br br0 ovs-vsctl add-port br0 eth0

    Add VM3 to VLAN 100:

    ovs-vsctl add-port br0 tap0 tag=100

    Add VM4 to VLAN 200:

    ovs-vsctl add-port br0 tap1 tag=200

6.3.11 openstack-service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

openstack-service start /stop

openstack-status


neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugin.ini upgrade head

neutron-db-manage

openstack-db --service neutron --update

openstack-db --service keystone --update


6.3.12 Using VXLAN Tenant Networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

vi /etc/neutron/plugins/openvswitch/ovs_neutron_plugin.ini
[OVS]
tenant_network_type=vxlan
tunnel_type=vxlan

[AGENT]
tunnel_types=vxlan

6.3.13 OpenvSwitch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Open vSwitch commands:
  init                        initialize database, if not yet initialized
  show                        print overview of database contents
  emer-reset                  reset configuration to clean state

Bridge commands:
  add-br BRIDGE               create a new bridge named BRIDGE
  add-br BRIDGE PARENT VLAN   create new fake BRIDGE in PARENT on VLAN
  del-br BRIDGE               delete BRIDGE and all of its ports
  list-br                     print the names of all the bridges
  br-exists BRIDGE            exit 2 if BRIDGE does not exist
  br-to-vlan BRIDGE           print the VLAN which BRIDGE is on
  br-to-parent BRIDGE         print the parent of BRIDGE
  br-set-external-id BRIDGE KEY VALUE  set KEY on BRIDGE to VALUE
  br-set-external-id BRIDGE KEY  unset KEY on BRIDGE
  br-get-external-id BRIDGE KEY  print value of KEY on BRIDGE
  br-get-external-id BRIDGE  list key-value pairs on BRIDGE

Port commands (a bond is considered to be a single port):
  list-ports BRIDGE           print the names of all the ports on BRIDGE
  add-port BRIDGE PORT        add network device PORT to BRIDGE
  add-bond BRIDGE PORT IFACE...  add bonded port PORT in BRIDGE from IFACES
  del-port [BRIDGE] PORT      delete PORT (which may be bonded) from BRIDGE
  port-to-br PORT             print name of bridge that contains PORT

Interface commands (a bond consists of multiple interfaces):
  list-ifaces BRIDGE          print the names of all interfaces on BRIDGE
  iface-to-br IFACE           print name of bridge that contains IFACE

Controller commands:
  get-controller BRIDGE      print the controllers for BRIDGE
  del-controller BRIDGE      delete the controllers for BRIDGE
  set-controller BRIDGE TARGET...  set the controllers for BRIDGE
  get-fail-mode BRIDGE       print the fail-mode for BRIDGE
  del-fail-mode BRIDGE       delete the fail-mode for BRIDGE
  set-fail-mode BRIDGE MODE  set the fail-mode for BRIDGE to MODE

Manager commands:
  get-manager                print the managers
  del-manager                delete the managers
  set-manager TARGET...      set the list of managers to TARGET...

SSL commands:
  get-ssl                     print the SSL configuration
  del-ssl                     delete the SSL configuration
  set-ssl PRIV-KEY CERT CA-CERT  set the SSL configuration

Switch commands:
  emer-reset                  reset switch to known good state

Database commands:
  list TBL [REC]              list RECord (or all records) in TBL
  find TBL CONDITION...       list records satisfying CONDITION in TBL
  get TBL REC COL[:KEY]       print values of COLumns in RECord in TBL
  set TBL REC COL[:KEY]=VALUE set COLumn values in RECord in TBL
  add TBL REC COL [KEY=]VALUE add (KEY=)VALUE to COLumn in RECord in TBL
  remove TBL REC COL [KEY=]VALUE  remove (KEY=)VALUE from COLumn
  clear TBL REC COL           clear values from COLumn in RECord in TBL
  create TBL COL[:KEY]=VALUE  create and initialize new record
  destroy TBL REC             delete RECord from TBL
  wait-until TBL REC [COL[:KEY]=VALUE]  wait until condition is true
Potentially unsafe database commands require --force option.

Options:
  --db=DATABASE               connect to DATABASE
                              (default: unix:/var/run/openvswitch/db.sock)
  --no-wait                   do not wait for ovs-vswitchd to reconfigure
  --retry                     keep trying to connect to server forever
  -t, --timeout=SECS          wait at most SECS seconds for ovs-vswitchd
  --dry-run                   do not commit changes to database
  --oneline                   print exactly one line of output per command

Logging options:
  -vSPEC, --verbose=SPEC   set logging levels
  -v, --verbose            set maximum verbosity level
  --log-file[=FILE]        enable logging to specified FILE
                           (default: /var/log/openvswitch/ovs-vsctl.log)
  --syslog-target=HOST:PORT  also send syslog msgs to HOST:PORT via UDP
  --no-syslog             equivalent to --verbose=vsctl:syslog:warn

Active database connection methods:
  tcp:IP:PORT             PORT at remote IP
  ssl:IP:PORT             SSL PORT at remote IP
  unix:FILE               Unix domain socket named FILE
Passive database connection methods:
  ptcp:PORT[:IP]          listen to TCP PORT on IP
  pssl:PORT[:IP]          listen for SSL on PORT on IP
  punix:FILE              listen on Unix domain socket FILE
PKI configuration (required to use SSL):
  -p, --private-key=FILE  file with private key
  -c, --certificate=FILE  file with certificate for private key
  -C, --ca-cert=FILE      file with peer CA certificate

Other options:
  -h, --help                  display this help message
  -V, --version               display version information
6.3.14 OpenvSwitch  in Allinone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
All in one with ens8

ovs-vsctl add-br br-ens8

ovs-vsctl add-port br-ens8 ens8

ifconfig br-ens8 10.3.4.4 up


ip link set br-ens8 promisc on

ip link add proxy-br-eth1 type veth peer name eth1-br-proxy

ip link add proxy-br-ex type veth peer name ex-br-proxy

ovs-vsctl add-br br-eth1

ovs-vsctl add-br br-ex

ovs-vsctl add-port br-eth1 eth1-br-proxy

ovs-vsctl add-port br-ex ex-br-proxy

ovs-vsctl add-port br-ens8 proxy-br-eth1

ovs-vsctl add-port br-ens8 proxy-br-ex


ip link set eth1-br-proxy up promisc on

ip link set ex-br-proxy up promisc on

ip link set proxy-br-eth1 up promisc on

ip link set proxy-br-ex up promisc on

*router ping

ip netns

ip netns exec qdhcp-9cbd5dd0-928a-4808-ae34-4cc2563fa619 ip addr


route add -net 192.168.32.0/24 gw 10.3.4.100

10.3.4.4->10.3.4.100->192.168.32.1  Ok

6.3.15 openstack Allinone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

packstack_uninstall.sh

* httpd.service error
mv 10-keystone_wsgi_admin.conf 10-keystone_wsgi_admin.conf.back
mv 10-keystone_wsgi_main.conf 10-keystone_wsgi_main.conf.back

and  systemctl start httpd.service


6.3.16 openstack Neutron
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# source keystonerc_osx
# neutron net-create osxnet
# neutron subnet-create osxnet 192.168.32.0/24 --name osx_subnet --dns-nameserver 8.8.8.8
# neutron net-create ext_net --router:external=True

# neutron subnet-create --gateway 10.3.4.1 --disable-dhcp --allocation-pool start=10.3.4.100,end=10.3.4.200 ext_net 10.3.4.0/24 --name ext_subnet
neutron subnet-create   --disable-dhcp --allocation-pool start=10.3.4.100,end=10.3.4.200 ext_net 10.3.4.0/24 --name ext_subnet


# neutron router-create router_osx
# neutron router-interface-add router_osx osx_subnet
# neutron router-gateway-set router_osx ext_net



vi /root/allinone-answers.cfg

CONFIG_NEUTRON_OVS_VLAN_RANGES=physnet1:10:20
CONFIG_NEUTRON_OVS_BRIDGE_MAPPINGS=physnet1:br-ex




vi /etc/sysconfig/network-scripts/ifcfg-br-ex
DEVICE=br-ex
DEVICETYPE=ovs
TYPE=OVSBridge
BOOTPROTO=none
IPADDR=10.20.0.20
NETMASK=255.255.255.0
GATEWAY=10.20.0.1
DNS1=8.8.8.8
DNS2=8.8.4.4
ONBOOT=yes

vi /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
TYPE=OVSPort
DEVICETYPE=ovs
OVS_BRIDGE=br-ex
NM_CONTROLLED=no
ONBOOT=yes
IPV6INIT=no
USERCTL=no

vi /etc/neutron/l3_agent.ini
external_network_bridge = br-ens8

ip link set br-ens8 promisc on


* router iptables problem

ip netns
ip netns exec qrouter-742cd9c5-de1d-409e-a138-e120f2658222 iptables -S -t nat
ip netns exec qrouter-742cd9c5-de1d-409e-a138-e120f2658222 vi /etc/sysconfig/iptables

add security rule all icmp,tcp,udp,ssh for default rule
* key point
ip link set br-ens8 promisc on

ip netns exec qrouter-f39e7f50-5113-414c-98fa-a94dd7976c57 ifconfig
ip netns exec qrouter-f39e7f50-5113-414c-98fa-a94dd7976c57 ip link set qg-6b9a9a40-d7 promisc on
ip netns exec qrouter-f39e7f50-5113-414c-98fa-a94dd7976c57 ip link set qg-6b9a9a40-d7 promisc on




*DVR (Distributed Virtual Router)
Before Juno, when we deploy Openstack in production, there always is a painful point about L3 Agent:
High availability and performance bottleneck

6.3.17 openstack Cinder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

openstack cinder does not work in box, it need physical volume


*tgt
yum install scsi-target-utils

vi /etc/tgt/targets.conf

include /etc/cinder/volumes/*

vi /etc/cinder/cinder.conf
enabled_backends=lvmdriver-1,lvmdriver-2

[lvmdriver-1]
volume_group=cinder-volumes-1
volume_driver=cinder.volume.drivers.lvm.LVMISCSIDriver
volume_backend_name=LVM_iSCSI1

[lvmdriver-2]
volume_group=cinder-volumes-2
volume_driver=cinder.volume.drivers.lvm.LVMISCSIDriver
volume_backend_name=LVM_iSCSI2

$ cinder type-create lvm1
cinder type-create lvm2
$ cinder type-key lvm1 set volume_backend_name=LVM_iSCSI1
cinder type-key lvm2 set volume_backend_name=LVM_iSCSI2
$ cinder extra-specs-list (just to check the settings are there)


systemctl enable tgtd.service
systemctl start tgtd.service


Define an iscsi target name
tgtadm --lld iscsi --op new --mode target --tid 1 -T  iqn.2015-07.10.3.0.104:storage.disk1

tgtadm --lld iscsi --op show --mode target

tgtadm --lld iscsi --op new --mode logicalunit --tid 1 --lun 1 -b /dev/vdb

acl setting
tgtadm --lld iscsi --mode target --op bind --tid 1 -I ALL            // ALL
tgtadm --lld iscsi --mode target --op bind --tid 1 -I 192.168.2.48   //for special ip
tgtadm --lld iscsi --mode target --op bind --tid 1 -I 10.3.0.0/24    // area

tgtadm --lld iscsi --op new --mode target --tid 2 -T  iqn.2015-07.10.3.0.104:storage.disk2
tgtadm --lld iscsi --op new --mode logicalunit --tid 2 --lun 1 -b /dev/vdc

tgtadm --lld iscsi --mode account --op new --user ''tom'' --password ''tom''



*file disk
dd if=/dev/zero of=/fs.iscsi.disk bs=1M count=512
tgtadm --lld iscsi --op new --mode logicalunit --tid 0 --lun 1 -b /fs.iscsi.disk


tgtadm --lld iscsi --mode target --op show

netstat -tulpn | grep 3260



iscsiadm --mode discovery --type sendtargets --portal 10.3.0.104
not working properly
*iscsi initiator

 [root@www ~]# yum -y install iscsi-initiator-utils
[root@www ~]# vi /etc/iscsi/initiatorname.iscsi
# change to the same IQN you set on the iSCSI target server

InitiatorName=iqn.2014-12.world.server:www.server.world
[root@www ~]# vi /etc/iscsi/iscsid.conf
# line 54: uncomment

node.session.auth.authmethod = CHAP
# line 58,59: uncomment and specify the username and password you set on the iSCSI target server

node.session.auth.username = username

node.session.auth.password = password
[root@www ~]# systemctl start iscsid

[root@www ~]# systemctl enable iscsid
# discover target

[root@www ~]# iscsiadm -m discovery -t sendtargets -p 10.3.0.104

10.0.0.30:3260,1 iqn.2014-12.world.server:storage.target00

# confirm status after discovery

[root@www ~]# iscsiadm -m node -o show

# BEGIN RECORD 6.2.0.873-24
node.name = iqn.2014-12.world.server:storage.target00
node.tpgt = 1
node.startup = automatic
node.leading_login = No
...
...
...
node.conn[0].iscsi.IFMarker = No
node.conn[0].iscsi.OFMarker = No
# END RECORD

# login to the target

[root@www ~]# iscsiadm -m node --login

Logging in to [iface: default, target: iqn.2014-12.world.server:storage.target00, portal: 10.0.0.30,3260] (multiple)
Login to [iface: default, target: iqn.2014-12.world.server:storage.target00, portal: 10.0.0.30,3260] successful.

# confirm the established session

[root@www ~]# iscsiadm -m session -o show

tcp: [1] 10.0.0.30:3260,1 iqn.2014-12.world.server:storage.target00 (non-flash)
# confirm the partitions

[root@www ~]# cat /proc/partitions

major minor  #blocks  name

  11        0    1999872 sr0
   8        0  157286400 sda
   8        1     512000 sda1
   8        2  156773376 sda2
 253        0   52428800 dm-0
 253        1    6225920 dm-1
 253        2   98050048 dm-2
   8       16   20971520 sdb

***

vi /etc/cinder/cinder.conf
enabled_backends=lvmdriver-1

[lvmdriver-1]
volume_group=cinder-volumes-1
volume_driver=cinder.volume.drivers.lvm.LVMISCSIDriver
volume_backend_name=LVM_iSCSI1


pvcreate /dev/vdb
pvcreate /dev/sda


vgcreate cinder-volumes-1 /dev/vdb
vgcreate cinder-volumes-2 /dev/sda


systemctl restart openstack-cinder-volume.service


$ cinder type-create lvm1
$ cinder type-key lvm1 set volume_backend_name=LVM_iSCSI1

$ cinder type-create lvm_vdb
$ cinder type-key lvm_vdb set volume_backend_name=lvm_vdb

$ cinder type-create lvm_sda
$ cinder type-key lvm_sda set volume_backend_name=lvm_sda


systemctl restart openstack-cinder-api.service openstack-cinder-backup.service openstack-cinder-scheduler.service  openstack-cinder-volume.service


cinder type-list
cinder extra-specs-list





6.3.17 openstack Cinder with Glusterfs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://www.unixmen.com/install-glusterfs-server-client-centos-7/
http://slidedeck.io/jbernard/cinder-configuration

* On controller

yum install glusterfs-fuse

vi /etc/cinder/cinder.conf
enabled_backends=cindervol1,cindervol2

[cindervol1]
volume_backend_name=GLUSTER1
volume_driver=cinder.volume.drivers.glusterfs.GlusterfsDriver
glusterfs_shares_config=/etc/cinder/shares.conf
glusterfs_mount_point_base=/var/lib/cinder/mnt/gluster1

[cindervol2]
volume_backend_name=GLUSTER2
volume_driver=cinder.volume.drivers.glusterfs.GlusterfsDriver
glusterfs_shares_config=/etc/cinder/shares.conf
glusterfs_mount_point_base=/var/lib/cinder/mnt/gluster2

$ cinder type-create gfsvol1
$ cinder type-key gfsvol1 set volume_backend_name=GLUSTER1
$ cinder type-create gfsvol2
$ cinder type-key gfsvol2 set volume_backend_name=GLUSTER2

$ cinder extra-specs-list (just to check the settings are there)




$ cinder type-create lvm
$ cinder type-key lvm set volume_backend_name=LVM_iSCSI
$ cinder extra-specs-list (just to check the settings are there)



vi /etc/cinder/shares.conf

OpenStackServer3:cindervol1
OpenStackServer3:cindervol2

* Gluster Host

gluster peer probe OpenStackServer1
gluster peer probe OpenStackServer3

gluster pool list


>gluster
volume create cindervol1 rep 2 transport tcp OpenStackServer3:/var/lib/cinder/volumes OpenStackServer1:/var/lib/cinder/cindervol1 force
volume start cindervol1

volume create cindervol2 rep 2 transport tcp OpenStackServer3:/var/lib/cinder/volumes2 OpenStackServer1:/var/lib/cinder/cindervol2 force
volume start cindervol2

Create mount point and mount the volume on both nodes:

[root@glusterfs1 ~]# mount -t glusterfs OpenStackServer3:/cindervol1 /var/lib/cinder/mnt/gluster1/

[root@glusterfs2 ~]# mount -t glusterfs OpenStackServer3:/cindervol1 /var/lib/cinder/mnt/gluster1/



systemctl restart openstack-cinder-volume.service

test
cinder create --display-name test 2
cinder create --display-name test2 2

6.3.18 openstack Cinder with cindervolumes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# create new

[DEFAULT]
state_path=/var/lib/cinder
api_paste_config=api-paste.ini
enable_v1_api=true
osapi_volume_listen=0.0.0.0
osapi_volume_listen_port=8776
rootwrap_config=/etc/cinder/rootwrap.conf
auth_strategy=keystone
# specify Glance server

glance_host=10.3.0.102
glance_port=9292
# specify RabbitMQ server

rabbit_host=10.3.0.102
rabbit_port=5672
# RabbitMQ user for auth

#rabbit_userid=guest
rabbit_userid=guest

# RabbitMQ user's password for auth

rabbit_password=guest
rpc_backend=rabbit
# specify iSCSI target (it's just the own IP)

iscsi_ip_address=10.3.0.104
iscsi_port=3260
iscsi_helper=tgtadm
scheduler_driver=cinder.scheduler.filter_scheduler.FilterScheduler
volume_manager=cinder.volume.manager.VolumeManager
volume_api_class=cinder.volume.api.API
volumes_dir=$state_path/volumes
# auth info for MariaDB

[database]
connection=mysql://cinder:password@10.3.0.102/cinder
# auth info for Keystone

[keystone_authtoken]
auth_host=10.3.0.102
auth_port=35357
auth_protocol=http
admin_user=cinder
#admin_password=servicepassword
admin_password=
admin_tenant_name=service

6.3.19 openstack error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instance failed to spawn : you must call 'aug-init' first to initialize Augeas

out of physical memory



6.4 OpenStack Juno +OpenDaylight Helium
-------------------------------------------

https://www.rdoproject.org/Helium_OpenDaylight_Juno_OpenStack
https://wiki.opendaylight.org/view/OVSDB:Helium_and_Openstack_on_Fedora20#VMs


opendaylight litium

https://wiki.opendaylight.org/view/OpenDaylight_DLUX:DLUX_Karaf_Feature

