chapter 3 : MariaDB
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

 vim /etc/my.cnf.d/mysql-clients.cnf

 [client]
 default-character-set = utf8

3.1.2 대소문자 구분 설정
~~~~~~~~~~~~~~~~~~~~~~~~~

데이터베이스 대소문자 구분 안함 설정
::

 vim /etc/my.cnf.d/server.cnf

 [mysqld]
 lower_case_table_names = 1

3.2 사용자 추가/삭제 & 권한
----------------------------------

3.2.1 패스워드 재설정
~~~~~~~~~~~~~~~~~~~~~~~~~

데몬 종료 및 기동
::

 service mysqld stop

 mysqld --skip-grant-table 로 데몬을 기동한다.
 암호 없이 접속
 mysql -u root mysql
 use mysql;
 새로운 암호 설정
 update user set password=password('암호') where user='root';
 flush privileges;

데몬 재기동
::

 service mysqld stop
 service mysqld start


3.2.2 mysql 패스워드 복잡성 해지
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

validate_password 파일 변경
::

 cd /usr/lib64/mysql/plugin/
 mv validate_password.so validate_password.so1

 서비스 재시작
 service mysqld restart

패스워드 변경
::

 mysql -u root -p
 ALTER USER 'root'@'localhost' IDENTIFIED BY '패스워드';
 flush privileges;

3.3 사용자 추가/삭제 & 권한
----------------------------------

3.3.1 사용자 추가/삭제
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


3.3.2 데이터베이스 사용권한
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


3.4 MySQL/MariaDB 백업 & 복원
------------------------

3.4.1 Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MariaDB 설치 폴더에서 bin폴더 cmd 실행 후 작업

백업
::

 mysqldump -uroot -p 데이터베이스이름 > D:\원하는폴더경로\원하는파일명

복원
::

 mysql -uroot -p123 --default-character-set="utf8" nbsf_dev < D:\Algorithm\nbsf20170215

3.4.2 Linux
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


3.4.3 시스템 백업
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root 계정으로 백업
::

 mysqldump --default-character-set=utf8 --set-charset -unbsf -pnbsf nbsf_dev > nbsf_dev.dump

 분할시
 mysqldump --default-character-set=utf8 --set-charset -uroot -p nbsf_dev | split -b 700m - nbsf_dev.dump
 cat nbsf_dev.dump* > nbsf_dev.dump

Database 생성
::

 mysql 진입
 mysql -uroot -p
 삭제
 drop database nbsf_dev;
 생성
 CREATE DATABASE nbsf_dev DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

유저생성 및 권한 부여
::

 use mysql;
 생성
 create user 'nbsf'@'%' identified by 'nbsf';
 권한
 grant all privileges on nbsf_dev.* to 'nbsf'@'%' WITH GRANT OPTION;
 적용
 flush privileges;
 확인
 SHOW GRANTS FOR 'nbsf'@'%';

Database 복구
::

 mysql 리눅스 백업db 폴더 진입 후

 mysql -uroot -pnbsf --default-character-set="utf8" nbsf_dev < nbsf_dev.dump

Databases 용량확인
::

 SELECT table_schema, SUM((data_length+index_length)/1024/1024) MB FROM information_schema.tables GROUP BY 1;
 6.2    11:15 2568.54983045
        11:49 2569.54983045 30분 1MB
        12:54 2570.54983045 60분 1MB
        14:15 2570.54983045 80분 0MB
        17:08 2573.54983045 180분 3MB
 6.7    09:00 2625.56545545 112시간 52MB
        10:31 2625.56545545 90분 0MB
        11:44 2626.56545545 70분 1MB
        12:47 2627.56545545 60분 1MB
        15:10 2627.56545545 130분 0MB
        16:55 2629.56545545 100분 2MB
 6.8    09:40 2638.56545545 17시간 9MB
 6.19   18:00 2770.62795545 11.5일 132MB

3.5 HeidiSQL
------------------------

3.5.1 테이블 복사
~~~~~~~~~~~~~~~~~~~~~~~

테이블 컬럼 복사
::

 show create table 테이블명
 Create Table 쿼리를 복사하여 실행

테이블 데이터 복사
::

 INSERT ignore INTO 복제테이블 SELECT * FROM 원본테이블

3.5.2 테이블 데이터 삭제
~~~~~~~~~~~~~~~~~~~~~~

삭제할 데이터 확인
::

 select * from ta_eval_health_index2
 where REG_DTM < '2017-05-21'

삭제할 데이터가 맞으면 삭제
::

 delete from ta_eval_health_index2
 where REG_DTM < '2017-05-21'

