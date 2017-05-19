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
