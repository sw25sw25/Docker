chapter 2 : 명령어
==============================

2.1 CentOS
--------------------------

2.1.1 IP 설정

IP 설정
::

 vim /etc/sysconfig/network-scripts/ifcfg-eth0

 # 장치명, 첫번째 이더넷카드
 DEVICE=eth0

 # IP 부여 방식 결정, static 은 고정IP
 BOOTPROTO=static

 # 이더넷카드의 MAC 주소
 HWADDR=XX:XX:XX:XX:XX:X

 # GUI 모드에서의 편리한 네트워크설정 허용, TUI에선 필요없음
 NM_CONTROLLED=no

 # 시스템 시작시 자동으로 활성화
 ONBOOT=yes

 # Ethernet 에 대한 설정
 TYPE=Ethernet

 # 고유ID를 부여하는 것으로 자동으로 부여됨
 UUID=XXXXXXX-XXX-XXX-XXX-XXXXXXX

 # 브로드캐스트 지정
 BROADCAST=192.168.0.255

 # IP 주소 지정
 IPADDR=192.168.0.5

 # 서브넷마스크 지정
 NETMASK=255.255.255.0

 # 네트워크 지정
 NETWORK=192.168.0.0

 # Wake On Lan 기능 활성화, Ethtool 이 필요한데 CentOS 기본 설치되어 있음
 ETHTOOL_OPTS=wol g

 # 일반사용자의 eth0 제어 가능여부
 USERCTL=no

 # IPV6 사용여부
 IPV6INIT=no

SSH 고정IP
::

 vim /etc/sysconfig/network-scripts/ifcfg-eth1
 BOOTPROTO=static
 IPADDR=192.168.56.102
 NETMASK=255.255.255.0
 GATEWAY=192.168.56.1

 네트워크 재시작
 /etc/rc.d/init.d/network restart

2.1.2 날짜 & 시간 설정
~~~~~~~~~~~~~~~~~~~~~~~~~~~

현재 날짜 & 시간 확인
::

 date

시간 바꾸기
::

 date -s 시:분:초

날짜 바꾸기
::

 date -s '년-월-일 시:분:초'

 date -s 년-월-일
 이 경우 시간이 00:00:00

export JAVA_OPTS="-Djava.awt.headless=true -server -Xms2048m -Xmx4096m -XX:NewSize=512m -XX:MaxNewSize=1024m -XX:PermSize=512m -XX:MaxPermSize=1024m -XX:+DisableExplicitGC"
export CATALINA_OPTS="-Denv=product -Denv.servername=projectTomcat"

2.1.3 경로 설정
~~~~~~~~~~~~~~~~~~~

경로 확인
::

 env

경로 삭제
::

 unset JAVA_HOME

2.1.4 SCP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

scp 사용
::

 윈도우 접속 상태에서 파일 전송
 scp -옵션 [옮길파일] [서버계정@서버아이피:/저장공간]
 -r : 폴더 복사
 -v : 복사 과정
 -P : 포트 번호

 윈도우 접속 상태에서 파일 수신
 scp -옵션 [서버계정@서버아이피:/옮길파일] [옮길경로]

 scp -P 25109 root@180.182.63.23:/home/mysql/ ./
 scp nbsf2_20170524 -P 10420 root@110.93.129.14:/home/mysql/
 scp root@10.10.131.138:/drives/e/nbsf2_20170524 /root/mariadb_backup

2.1.5 기타
~~~~~~~~~~~~~~~~~~~~~~

UTF8 확인
::

 locale

로그 확인
::

 tail -f catalina.out

SELinux
::

 vi /etc/selinux/config

 SELINUX=disabled

실행중인 서비스 확인(방화벽 확인)
::

 service iptables status

방화벽 서비스 끄기
::

 /etc/rc.d/init.d/iptables stop
 /etc/rc.d/init.d/ip6tables stop

포트 확인
::

 netstat -an |grep 8080

프로세스 확인
::

 ps -ef |grep java

검색
::

 find 경로 -옵션 옵션에따른검색어
 -name  파일이름
 -user  소유자
 -type  타입
     d : directory
     f : regular file
     b: block device file
     c : character device fine,
     n: network sepecial file
     p: named pipe
     s: socket
 -size  파일사이즈 이상(100c, c는 Byte를 의미함)
 -mtime n일 이상 변경되지 않은 파일
 -atime n일 이상 엑세스되지 않은 파일

 find 경로 -