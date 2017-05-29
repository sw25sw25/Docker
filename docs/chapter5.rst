chapter 5 : Scouter의 구성
============================

5.1 Scouter의 구성
------------------------

https://www.slideshare.net/ienvyou/scouter-jboss

Server(Collector)
::

 Agent가 전송한 데이터 수집/처리

Host Agent
::

 OS의 CPU, Memory, Disk등의 성능 정보 전송

Java Agent
::

 실시간 서비스 성능 정보, Heap Memory, Thread 등 Java 성능 정보

Client(Viewer)
::

 수집된 성능 정보를 확인하기 위한 Client 프로그램

5.2 Scouter 설치
--------------------------------

5.2.1 Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scouter Server(Collector) 실행
::

 start-scouter-server.bat

Client(Viewer) 실행
::

 scouter.exe
 127.0.0.1:6100
 admin/admin

Host Agent 실행(Optional)
::

 start-scouter-host.bat

데모 시스템 실행(Tomcat with WAR)
::

 start-tomcat.bat

jmeter를 통한 가상의 부하 발생
::

 start-jmeter.bat


5.2.2 Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

권한 설정
::

 chmod -fR 755 *

Scouter 서버 설정
::

 /usr/local/scouter/demo-env1/scouter/server/conf/scouter.conf

 net_tcp_listen_port=6100
 net_udp_listen_port=6100
 db_dir=./database
 log_dir=./logs

 /usr/local/scouter/demo-env1/scouter/server/startup.sh

 -Xms2048m -Xmx2048m

Scouter Server(Collector) 실행
::

 ./start-scouter-server.sh

Client(Viewer) 실행
::

 scouter.exe
 192.168.56.1:6100
 admin/admin

Host Agent 설정
::

 /usr/local/scouter/demo-env1/scouter/agent.host/conf/scouter.conf

 # Scouter Server IP Address (Default : 127.0.0.1)
 net_collector_ip=192.168.0.147

 # Scouter Server Port (Default : 6100)
 net_collector_udp_port=6100
 net_collector_tcp_port=6100

 # Log directory(Default : ./logs)
 log_dir=./logs

 -Xmx512m 해당 하는 부분을 장비 성능등에 맞게 설정
 Ex) -Xms512m -Xmx512m

 에이전트 호스트는 운영체제의 CPU, 메모리 정보를 수집하는 역할

Host Agent 실행(Optional)
::

 ./start-scouter-host.sh

모니터링 대상 WAS 설정
::

 /usr/local/scouter/demo-env1/scouter/agent.java/conf/jboss_standalone_ha_11_143.conf
 # Scouter Server IP Address (Default : 127.0.0.1)
 # Data 수집 ( Collector & Server ) 서버
 net_collector_ip=192.168.0.147

 # Scouter Server Port (Default : 6100)
 net_collector_udp_port=6100
 net_collector_tcp_port=6100

 # Scouter Name(Default : tomcat1)
 # agent name 설정
 obj_name=jboss_standalone_ha_11_143

 trace_interservice_enabled=true
 # Hooking 하여 기록할 method의 pattern 정의
 # 여러개인 경우 comma(,)로 구분
 # format : package.Class.method,package.Class2.method2
 hook_method_patterns=org.mybatis.jpetstore.*.*

 # jdbc leak profile 설정
 # ibatis 와 같은 framework 을 사용하는 경우 hook_connection_open_patterns 을 설정
 # format : hook_connection_open_patterns=org.springframework.jdbc.datasource.AbstractDriverBasedDataSource.getConnection
 profile_connection_open_enabled=true

 # 서비스 연계 추적으로 HTTP로 요청하는 서비스 간 연결 추적이 활성화
 trace_interservice_enabled=false

JBoss 실행 파일 scouter agent.java 설정 적용
::

 /usr/local/scouter/demo-env1/scouter/server/env.sh
 /opt/was/servers/standalone_ha_11/bin/env.sh 설정

 # Byte Code Instrumentation 기법으로 실제 실행 환경의 동작 모니터링을 위한 agent Library loading 위한 설정
 -javaagent

 # agent.java 의 설정 파일의 위치를 지정
 -Dscouter.config

 JBoss의 경우에는 OSGI 클래스로더 구조로 인하여standalone.conf 혹은 domain.conf 파일 등과 같은 config 설정 파일 혹은 실행 파일 부분에 다음과 같이 적용
 -Djboss.modules.system.pkgs=org.jboss.byteman,scouter
 export JAVA_OPTS=" $JAVA_OPTS -Djboss.modules.system.pkgs=org.jboss.byteman,scouter" JBoss 기동 스크립트에 Scouter에 대한 설정을 통해 BCI 작업이 이루어지도록 함

데모 시스템 실행(Tomcat with WAR)
::

 ./start-tomcat.sh
