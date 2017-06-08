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

