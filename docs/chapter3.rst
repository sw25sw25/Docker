chapter 3 :MariaDB
============================

3.1 MySQL/MariaDB 백업 & 복원
------------------------

3.1.1 Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MariaDB 설치 폴더에서 bin폴더 cmd 실행 후 작업

백업
::

    mysqldump -uroot -p 데이터베이스이름 > D:\원하는폴더경로\원하는파일명

복원
::

    mysql -uroot -p123 --default-character-set="utf8" nbsf_dev < D:\Algorithm\nbsf20170215

3.1.2 Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    mysqldump -u[아이디] -p[패스워드] > [저장파일명].sql

MySQL/MariaDB 전체 데이터베이스를 백업
::

    mysqldump -uroot -p -A > backup_full.sql

생성된 덤프를 이용한 복원
::

    mysql -uroot -p < backup_full.sql

sw_test 라는 데이터베이스만 백업
::

    mysqldump -uroot -p sw_test > backup_sw_test.sql

sw_test 데이터베이스의 tbl_a라는 테이블만 백업
::

    mysqldump -uroot -p sw_test tbl_a > backup_sw_test_tbl_a.sql

sw_test 데이터베이스의 tbl_a테이블의 emp_no가 100 이상 200이하의 데이터만 백업
::

    mysqldump -uroot -p sw_test tbl_a -w'emp_no >= 100 and emp_no <= 200' > backup_sw_test_tbl_a.sql

실제 데이터백업은 받지 않고 테이블 definition만 백업
::

    mysqldump -uroot -p sw_test --no-data > backup_sw_test_definition.sql


테스트
::

	aerkjhkabhcmew

쓰기

3.1.3 MariaDB 계정 생성
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

사용자 추가
::

 GRANT ALL PRIVILEGES ON dbname.* TO username@localhost IDENTIFIED BY 'password';
                   데이터베이스.권한 사용자아이디@호스트               패스워드
 username(사용자아이디)은 dbname(데이터베이스)에 대해 모든 권한을 가지고 있고, localhost에만 접속할 수 있다.
 모든 호스트에 접속하려면 localhost 대신 ‘%’ 입력

사용자 삭제
::

 DLETE FROM USER WHERE USER='username';
 FLUSH PRIVILEGES;

MariaDB UTF8 설정
::

 MariaDB :: show variables like 'c%';

 vim /etc/my.cnf.d/server.cnf

 [mysqld]
 init_connect = SET collation_connection = utf8_general_ci
 character-set-server = utf8
 collation-server = utf8_general_ci
 init_connect = SET NAMES utf8

 vim /etc/my.cnf.d/mysql-clients.cnf

 [client]
 default-character-set = utf8







spc 사용
::

 scp -P 25109 root@180.182.63.23:/home/mysql/ ./
 scp nbsf2_20170524 -p 10420 root@110.93.129.14:/home/mysql/
 scp root@10.10.131.138:/drives/e/nbsf2_20170524 /root/mariadb_backup
