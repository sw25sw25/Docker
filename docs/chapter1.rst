chapter 1: 설치
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

 yum list installed java*jdk

확인된 기존 자바 삭제
::

 yum remove 검색된 openjdk 이름

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

 # Get Config
 [ -f 톰캣폴더/conf/server.xml ] && [ -f 톰캣폴더/conf/web.xml ] || exit 0

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

8080 포트 확인
::

 netstat -ntl


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

기존 httpd 삭제
::

 yum remove httpd

