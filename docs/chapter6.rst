chapter 6 : 프로젝트 지원
============================

6.1 레드마인 설정
----------------------------

6.1.1 메일 설정
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

메일 설정
::

 /opt/redmine-3.3.3-0/apps/redmine/htdocs/config/configuration.yml
 띄어쓰기 주의!!

 default:
   # Outgoing emails configuration
   # See the examples below and the Rails guide for more configuration options:
   # http://guides.rubyonrails.org/action_mailer_basics.html#action-mailer-configuration
   email_delivery:
     delivery_method: :smtp
     smtp_settings:

       address: smtp.gmail.com
       port: 587
       domain: example.net
       authentication: :login
       user_name: 아이디@gmail.com
       password: 비밀번호

 재시작
 cd /opt/redmine-3.2.3-1
 ./ctlscript.sh restart apache

6.1.2 HTTPS 강제 리다이렉션
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

레드마인 설정
::

 vim /opt/redmine-3.2.3-1/apps/redmine/conf/httpd-prefix.conf

 맨 위에
 RewriteEngine On
 RewriteCond %{HTTPS} !=on
 RewriteRule ^/(.*) https://%{SERVER_NAME}/$1 [R,L]

 재시작
 cd /opt/redmine-3.2.3-1
 ./ctlscript.sh restart apache

멘티스 설정
::

 vim /opt/mantis-2.3.1-0/apps/mantis/conf/httpd-prefix.conf

 맨 위에
 RewriteEngine On
 RewriteCond %{HTTPS} !=on
 RewriteRule ^/(.*) https://%{SERVER_NAME}/$1 [R,L]

 재시작
 cd /opt/mantis-2.3.1-0
 ./ctlscript.sh restart apache

6.1.3 SSL 인증서(도메인 주소 필요)
~~~~~~~~~~~~~~~~~~~~~~~~~~

비공개 키 만들기
::

 openssl genrsa -out /opt/redmine-3.2.3-1/apache2/conf/server.key 2048

인증서 만들기
::

 openssl req -new -key /opt/redmine-3.2.3-1/apache2/conf/server.key -out installdir/apache2/conf/cert.csr

설치
::

 cd /usr/local
 yum install epel-release
 rpm -ivh https://rhel6.iuscommunity.org/ius-release.rpm
 yum install git python27 python27-devel python27-pip python27-setuptools python27-virtualenv python27-libs
 git clone https://github.com/letsencrypt/letsencrypt

실행
::

 chattr -i /usr/bin/gcc /usr/bin/g++ (실행 x)
 cd /usr/local/letsencrypt
 /usr/local/letsencrypt/letsencrypt-auto certonly
 chmod 700 /usr/bin/gcc /usr/bin/g++;chattr +i /usr/bin/gcc /usr/bin/g++

6.2 gitlab
----------------------------

6.2.1 설치
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://about.gitlab.com/downloads/#centos6

설치파일 실행
::

 rpm -ivh gitlab-ce-9.2.1-ce.0.el6.x86_64.rpm

재구성
::

 gitlab-ctl reconfigure

6.2.2 설정

실행
::

 # Start all GitLab components
 /opt/gitlab/bin/gitlab-ctl start

 # Stop all GitLab components
 /opt/gitlab/bin/gitlab-ctl stop

 # Restart all GitLab components
 /opt/gitlab/bin/gitlab-ctl restart