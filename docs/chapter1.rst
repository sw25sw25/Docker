chapter 1 : 설치
==================

1.1 CentOS
-------------------

1.1.1 버전 확인
~~~~~~~~~~~~~~~~~~~

CentOS 버전 확인
::

 cat /etc/centos-release

커널 버전 확인
::

 uname -r

1.1.2 자바 설치
~~~~~~~~~~~~~~~~~~

기존 자바 설치 파일 확인
::

 rpm -qa | grep java

확인된 기존 자바 삭제
::

 yum remove 검색된openjdk이름

자바.tar.gz 압축 풀기(/usr/local) 및 심볼릭 링크
::

 tar -zxvf 파일명.tar.gz
 ln -s 링크파일 링크명

환경변수 설정 및 적용
::

 vim /etc/profile

 export JAVA_HOME=/usr/local/java
 export CLASSPATH=.:$JAVA_HOME/lib/tools.jar
 export PATH=$PATH:$JAVA_HOME/bin

 source /etc/profile

자바 버전 확인
::

 java -version
 javac -version

1.1.3 톰캣 설치
~~~~~~~~~~~~~~~

톰캣.tar.gz 압축 풀기(/usr/local) 및 심볼릭 링크
::

 tar -zxvf 파일명.tar.gz
 ln -s 링크파일 링크명

환경변수 설정 및 적용
::

 vim /etc/profile

 export CATALINA_HOME=/usr/local/tomcat
 export CLASSPATH=$CATALINA_HOME/lib-jsp-api.jar:$CATALINA_HOME/lib/servlet-api.jar
 export PATH=$CATALINA_HOME/bin

 source /etc/profile

8080포트 방화벽 해제
::

 vim /etc/sysconfig/iptables

 iptables -A INPUT -m state --state NEW -p tcp --dport 8080 -j ACCEPT

 service iptables save
 service iptables restart

톰캣 서버 작동 및 중지
::

 /usr/local/tomcat/bin/startup.sh
 /usr/local/tomcat/bin/shutdown.sh

부팅 시 자동실행 설정
::

 vim /etc/rc.d/init.d/tomcat

 #!/bin/sh
 # chkconfig: 345 90 90
 # description: init file for tomcat
 # processname: tomcat

 export JAVA_HOME=/usr/local/java
 export CATALINA_HOME=/usr/local/tomcat
 export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$CATALINA_HOME/lib-jsp-api.jar:$CATALINA_HOME/lib/servlet-api.jar
 export PATH=$PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin

 # Get Config
 [ -f /usr/local/tomcat/conf/server.xml ] && [ -f /usr/local/tomcat/conf/web.xml ] || exit 0

 source /etc/profile

 # Source function library
 . /etc/rc.d/init.d/functions

 # caution :
 #           variable=<value> space between variable and value is not allowed
 RETVAL=0
 prog=tomcatd

 # Start function
 start()
 {
   echo -n "Starting $prog : "
   daemon $CATALINA_HOME/bin/startup.sh
   RETVAL=$?
   echo
   touch /var/lock/subsys/tomcat
   return $RETVAL
 }

 # Stop fucntion
 stop()
 {
   echo -n "Stopping $prog : "
   daemon $CATALINA_HOME/bin/shutdown.sh
   RETVAL=$?
   echo
   rm -f /var/lock/subsys/tomcat
   return $RETVAL
 }

 # Restart function
 restart()
 {
   stop
   start
 }

 # See how we were called
 case "$1" in
      start)
            start
            ;;
      stop)
            stop
            ;;
      restart)
            restart
            ;;
      *)
            echo $"Usage : $0 {start|stop|restart}"

 esac

 exit $RETVAL

실행권한 부여
::

 chmod u+x /etc/rc.d/init.d/tomcat
 chmod 755 /etc/rc.d/init.d/tomcat

작동 테스트
::

 /etc/rc.d/init.d/tomcat start
 /etc/rc.d/init.d/tomcat restart
 /etc/rc.d/init.d/tomcat stop

chkconfig 등록
::

 chkconfig --add tomcat
 chkconfig --list tomcat
 tomcat  0:해제	1:해제	2:해제	3:활성	4:활성	5:활성	6:해제
 reboot

 * 만약 3~5번이 활성화 되있지 않다면, chkconfig --level 345 tomcat on

8080 포트 확인 및 프로세스 확인
::

 netstat -ntl
 ps -ef | grep tomcat


1.1.4 MariaDB 설치(tar.gz)
~~~~~~~~~~~~~~~~~~~~

MariaDB 설치 확인
::

 rpm -qa | grep MariaDB

MariaDB 압축 해제 및 파일 이동
::

 tar -zxvf 파일명.tar.gz
 rm -rf 파일명.tar.gz
 mv 마리아폴더 /usr/local

MariaDB 심볼릭 링크
::

 ln -s 마리아폴더 mariadb

MariaDB 사용자 및 그룹 추가(선택)
::

 useradd -M mariadb
 usermod -d 마리아폴더 mariadb
 grep mariadb /etc/passwd

 groupadd mariadb
 useradd -g mariadb mariadb

MariaDB 사용자 권한 설정(선택)
::

 chown mariadb.mariadb -R 마리아폴더
 chmod 755 -R 마리아폴더

my.cnf 복사
::

 cp 마리아폴더/support-files/아래파일명 /etc/my.cnf
 시스템 메모리가 4G이상일 때 : my-innodb-heavy-4G.cnf
 시스템 메모리가 1G~2G일 때 : my-huge.cnf
 시스템 메모리가 512MB정도 일 때 : my-large.cnf
 시스템 메모리가 32MB~64MB정도 일 때 : my-medium.cnf
 시스템 메모리가 64MB이하일 때 : my-small.cnf

한글(my.cnf에 내용 추가)
::

 character-set-server=utf8
 collation-server=utf8_general_ci

실행데몬 복사
::

 cp 마리아폴더/support-files/mysql.server /etc/init.d/mysqld

사용자 권한 설정(선택)
::

 chown mariadb.mariadb /etc/init.d/mysqld
 chmod 750 /etc/init.d/mysqld

실행데몬 수정
::

 vim /etc/init.d/mysqld

 basedir=마리아폴더
 datadir=마리아폴더/data

PATH 설정 및 적용
::

 vim /etc/profile

 PATH=$PATH:마리아폴더/bin

 source /etc/profile

MariaDB 실행
::

 service mysqld start

부팅 시 자동시작
::

 chkconfig mysql on
 chkconfig --list mysql

 2~5:on

보안설정
::

 ./마리아폴더/bin/mysql_secure_installation –basedir=마리아폴더

 Set root password? [Y/n] y
 Remove anonymous users? [Y/n] y
 Disallow root login remotely? [Y/n] y
 Remove test database and access to it? [Y/n] y
 Reload privilege tables now? [Y/n] y

접속확인
::

 mysql -uroot -p

# DB생성 (mariadb 계정으로 로그인)
/usr/local/mariadb/scripts/mysql_install_db –user=mariadb –basedir=/usr/local/mariadb –datadir=/usr/local/mariadb/data
rpm 설치
::

 rpm -qa 'mysql*'
 rpm -ivh MariaDB-*

1.1.5 MairaDB 설치(rpm)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

기존 설치 파일 확인
::

 rpm -qa | grep mysql

기존 설치 파일 삭제
::

 rpm -e --nodeps mysql-libs-5.1.73-8.el6_8.x86_64

MariaDB.rpm 서명 체크(선택)
::

 rpm --checksig $(find . -name '*.rpm')

MariaDB.rpm 서명 가져오기(선택)
::

 gpg --keyserver hkp://pgp.mit.edu --recv-keys 1BB943DB
 gpg --export --armour 1BB943DB > mariadb-signing-key.asc
 rpm --import mariadb-signing-key.asc
 rpm -qa gpg-pubkey*

 rpm --checksig $(find . -name '*.rpm')

perl-DBI 설치 및 MariaDB 설치
::

 rpm -Uvh perl-DBI-*
 rpm -Uvh MariaDB-*

설치 확인 및 실행
::

 rpm -qa | grep MariaDB

 /etc/init.d/mysql start

비밀번호 설정
::

 /usr/bin/mysqladmin -u root password '패스워드'


1.1.6  아파치 설치
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

기존 아파치 설치 파일 확인
::

 rpm -qa | grep httpd

기존 httpd 삭제
::

 rpm -e --nodeps 검색된httpd이름

httpd 설치
::

 rpm -ivh httpd-*

기본 설정
::

 vim /etc/httpd/conf/httpd.conf

아파치에서 .php 파일 등 연결
::

 AddType application/x-httpd-php .php .ph .phtml .php3 .php4 .sql .inc .html .htm
 AddType application/x-httpd-php-source .phps

ServerName 변경
::

 ServerName 127.0.0.1:80

방화벽 설정
::

 vim /etc/sysconfig/iptables

 -A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT

 /etc/init.d/iptables restart

자동실행 설정
::

 chkconfig httpd on
 chkconfig --list httpd
 httpd    0:off	1:off	2:on	3:on	4:on	5:on	6:off

동작 확인
::

 ps -ef | grep httpd


1.1.7 mod_JK
~~~~~~~~~~~~~~~~~~~~~~~

파일 복사
::

 /etc/httpd/modules/mod_jk.so

 SELinux 를 사용한다면 mod_jk.so 에 httpd_modules_t Context 가 설정되어야 apache httpd 가 읽을 수 있다. 다음 명령어로 설정하자.
 chcon -u system_u -r object_r -t httpd_modules_t /etc/httpd/modules/mod_jk.so

Apache 웹서버에서 mod_jk 설정
::

 vim /etc/httpd/conf/httpd.conf

 LoadModule jk_module modules/mod_jk.so

 ServerName localhost

 include /etc/httpd/conf.d/mod_jk.conf

 vim /etc/httpd/conf.d/mod_jk.conf

 <IfModule mod_jk.c>
  # Where to find workers.properties
  # JkWorkersFile /etc/httpd/conf/workers_jk.properties

  # Where to put jk shared memory
  JkShmFile run/mod_jk.shm

  # Where to put jk logs
  JkLogFile logs/mod_jk.log

  # Set the jk log level [debug/error/info]
  JkLogLevel info

  # Select the timestamp log format
  JkLogStampFormat "[%a %b %d %H:%M:%S %Y] "

  # If you want to put all mounts into an external file
  # that gets reloaded automatically after changes
  # (with a default latency of 1 minute),
  # you can define the name of the file here.
  JkMountFile /etc/httpd/conf/uriworkermap.properties
 </IfModule>

mod_jk worker 설정
::

 vim /etc/httpd/conf/workers_jk.properties

 worker.list=worker1, worker2

 worker.worker1.port=8009
 worker.worker1.host=server1
 worker.worker1.type=ajp13
 worker.worker1.lbfactor=1

 ## server 2
 worker.worker2.port=8009
 worker.worker2.host=server2
 worker.worker2.type=ajp13
 worker.worker2.lbfactor=1

톰캣 연결 설정
::

 vim /usr/local/tomcat/conf/server.xml
 tomcat 은 기본 URIEncoding 이 ISO-8859-1 이므로 한글이 깨지므로 모든 커넥터 설정에 URIEncoding="UTF-8" 을 추가해야 한다.
 <Connector port="8009" protocol="AJP/1.3" redirectPort="8443" URIEncoding="UTF-8"/>

어떤 url 요청에 대해 tomcat 과 연계할지 설정한다.
::

 vim /etc/httpd/conf/uriworkermap.properties
 ## Mapping the URI /service1 under worker1
 /service1/*.do=worker1
 /service1/*.jsp=worker1

 # /service2 요청으로 들어온 것은 worker2 로 mount
 /service2/*=worker2

 # png와 jpg 는 apache 가 처리
 !/service2/*.png=worker2
 !/service2/*.jpg=worker2

 ## 아래와 같이 설정하면 모든 요청(jsp, do, image, js등)을 tomcat으로 보내서 처리한다.
 # /*=worker1

테스트
::

 apachectl start
 catalina.sh start

 http://아이피/index.jsp 으로 호출이 되면 성공