chapter2   명령어
==============================

2.1 CentOS
--------------------------

2.1.1 날짜 & 시간 설정
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

2.1.2 경로 설정
~~~~~~~~~~~~~~~~~~~

경로 확인
::

 env

경로 삭제
::

 unset JAVA_HOME

2.1.2 SPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

spc 사용
::

 scp -P 25109 root@180.182.63.23:/home/mysql/ ./
 scp nbsf2_20170524 -p 10420 root@110.93.129.14:/home/mysql/
 scp root@10.10.131.138:/drives/e/nbsf2_20170524 /root/mariadb_backup

기타
~~~~~~~~~~~~~~~~~~~~~~

UTF8 확인
::

 locale

로그 확인
::

 tail -f catalina.out

포트 확인
::

 netstat -an |grep 8080

프로세스 확인
::

 ps -ef |grep java
