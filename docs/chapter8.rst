chapter 7 : 설정
==================================

7.1 tomcat
---------------------------

vim /etc/init.d/tomcat
::

 export JAVA_HOME=/usr/local/src/jdk1.7.0_80
 export PATH=$JAVA_HOME/bin:$PATH

 export JAVA_OPTS="-Djava.awt.headless=true -server -Xms2048m -Xmx4096m -XX:NewSize=512m -XX:MaxNewSize=1024m -XX:PermSize=512m -XX:MaxPermSize=1024m -XX:+DisableExplicitGC"

 export CATALINA_OPTS="-Denv=product -Denv.servername=projectTomcat"

 export CATALINA_HOME=/usr/local/src/tomcat7

 #. /etc/profile

 case "$1" in

     start)

         echo "Starting tomcat: "

         #su - tomcat -c $CATALINA_HOME/bin/startup.sh
         $CATALINA_HOME/bin/startup.sh

         ;;

     stop)

         echo "Shutting down tomcat: "

         #su - tomcat -c $CATALINA_HOME/bin/shutdown.sh
         $CATALINA_HOME/bin/shutdown.sh

         ;;

     restart)

         echo "Restarting tomcat: "

         #su - tomcat -c $CATALINA_HOME/bin/shutdown.sh; su - tomcat -c $CATALINA_HOME/bin/startup.sh
         $CATALINA_HOME/bin/shutdown.sh; su - tomcat -c $CATALINA_HOME/bin/startup.sh

         ;;

     *)

         echo "Usage: service tomcat {start|stop|restart}"

         exit 1

 esac

 exit 0


7.2 HTTPS(톰캣 사설 인증서)
--------------------------------

7.2.1 톰캣 사설 인증서 올리기
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows에서 cmd 실행
::

 keytool.exe(JDK_HOME/bin) 이 실행되는지 확인(실행안되면 환경변수에 path 추가)
 keytool.exe

 인증서를 생성할 디렉토리로 이동
 cd C:\privateCert

서버키 생성(이름은 변경가능:TestServer)
::

 keytool -genkey -keyalg RSA -sigalg SHA1withRSA -alias TestServer -keysize 2048 -keystore TestServer.key
 비밀번호 등 입력(국가 코드 : KR)
 TestServer.key 파일 생성 여부 확인

인증서 생성(이름은 변경가능:TestServer)
::

 C:\privateCert>keytool -certreq -alias TestServer -keyalg RSA -sigalg SHA1withRSA -file TestServer.csr -keystore TestServer.key
 TestServer.csr 파일 생성 여부 확인

서버에서 설정
::

 server.xml 위치로 이동(톰캣:TOMCAT_HOME/conf, 이클립스:Server/해당WAS)
 SSL 설정 주석 풀기(8443 으로 검색하면 나옴)
     <Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"
                maxThreads="150" scheme="https" secure="true"
                clientAuth="false" sslProtocol="TLS"
                keystoreFile="/root/privateCert/TestServer.key" keystorePass="tmddhks" />

 톰캣 restart

7.2.2 톰캣 시작페이지 설정
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

8080 시작페이지 설정
::

 </Host> 앞에
 <Context path="/" docBase="/usr/local/apache-tomcat-7.0.78/webapps/AMS-1.0" debug="0" reloadable="true" />

7.2.3 톰캣 매니저 권한
~~~~~~~~~~~~~~~~~~~~~~~

매니저 권한 설정
::

 vim $CATALINA_HOME/conf/tomcat-users.xml
 <tomcat-users>
 <role rolename="admin-gui"/>
 <role rolename="manager-gui"/>
 <user username="이름" password="패스워드" roles=" admin-gui ,manager-gui"/>
 </tomcat-users>

7.3 vboxvmservice(VirtualBox 자동실행)
----------------------------------------

7.3.1 설정
~~~~~~~~~~~~~~~~~~~~

http://blog.djjproject.com/184

서비스 설정
::

 C:\vms\VBoxVmService.ini

 ShutdownMethod=
 savestate(윈도우 종료시 상태를 저장하고 부팅시 저장된 상태로 다시 시작)
 acpipowerbutton(VM에 종료명령을 보내 종료 후 윈도우 종료)


