chapter 7 : 설정
==================================

7.1 tomcat
---------------------------

vim /etc/init.d/tomcat
::

 JAVA_HOME=/usr/local/src/jdk1.7.0_80
 export JAVA_HOME
 export PATH=$JAVA_HOME/bin:$PATH

 export JAVA_OPTS="-Djava.awt.headless=true -server -Xms2048m -Xmx4096m -XX:NewSize=512m -XX:MaxNewSize=1024m -XX:PermSize=512m -XX:MaxPermSize=1024m -XX:+DisableExplicitGC"

 export CATALINA_OPTS="-Denv=product -Denv.servername=projectTomcat"


 CATALINA_HOME=/usr/local/src/tomcat7
 export CATALINA_HOME
