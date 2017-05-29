chapter 6 : Redmine
============================

6.1 레드마인 설정
----------------------------
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
 cd /usr/local/redmine-3.3.3-0
 ./ctlscript.sh restart apache