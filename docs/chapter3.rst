chapter 3 :MariaDB
============================

3.1 기본 설정
-------------------------------

3.1.1 UTF8 설정
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

 MariaDB :: show variables like 'c%';

 vim /etc/my.cnf.d/server.cnf

 [mysqld]
 init_connect = SET collation_connection = utf8_general_ci
 character-set-server = utf8
 collation-server = utf8_general_ci
 init_connect = SET NAMES utf8

 #데이터베이스 대소문자 구분 안함 설정
 lower_case_table_names = 1

 vim /etc/my.cnf.d/mysql-clients.cnf

 [client]
 default-character-set = utf8

3.1.2 대소문자 구분 설정

3.2 사용자 추가/삭제 & 권한
----------------------------------

3.2.1 사용자 추가/삭제
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

사용자 확인
::

 root 계정으로 접속
 mysql -uroot -p

 use mysql;
 select host, user, password from user;

 host는 사용자 아이디 뒤에 @localhost, '%'에 따라서 외부 접근이 허용되는 권한을 줄 수 있다.
 localhost는 내부접근, '%'는 외부접근

사용자 추가
::

 create user 사용자아이디@localhost identified by 'password';
                            '%'

사용자 삭제
::

 delete from user where user ='사용자아이디';


3.2.2 데이터베이스 사용권한
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

데이터베이스 사용권한 부여
::

 grant all privileges on 데이터베이스.테이블 to 사용자아이디@호스트 identified by '패스워드';
 모든 테이블 *, 모든 호스트'%'

 변경된 권한 적용
 flush privileges;

데이터베이스 사용권한 삭제
::

 revoke all on 데이터베이스.테이블 from 사용자이름@호스트

권한 확인
::

 show grants for 사용자아이디@'%';


3.3 MySQL/MariaDB 백업 & 복원
------------------------

3.3.1 Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MariaDB 설치 폴더에서 bin폴더 cmd 실행 후 작업

백업
::

    mysqldump -uroot -p 데이터베이스이름 > D:\원하는폴더경로\원하는파일명

복원
::

    mysql -uroot -p123 --default-character-set="utf8" nbsf_dev < D:\Algorithm\nbsf20170215

3.3.2 Linux
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

