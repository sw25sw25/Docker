chapter 4 : 알고리즘
============================


4.1 알고리즘 설정
------------------------

4.1.1 알고리즘
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

 export DAEMON_NAME=ams-algorithm
 export DAEMON_HOME=/home/algorithm/ams
 export MAIN=ams-algorithm.jar

 export JAVA=/home/algorithm/ams/jre1.8.0_111/bin/java
 export XMS=-Xms1024m
 export XMX=-Xmx2048m
 export JVM_OPTION="-Dfile.encoding=UTF-8 -Dserver.port=24119"

4.1.2 dev 알고리즘
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

개발서버 알고리즘
::

 #!/bin/bash
 # description: ITX
 # chkconfig: 2345 20 80
 # processname: java

 export DAEMON_NAME=ams-algorithm
 export DAEMON_HOME=/home/algorithm/ams
 export MAIN=ams-algorithm.jar

 export JAVA=/home/algorithm/ams/jre1.8.0_111/bin/java
 export XMS=-Xms1024m
 export XMX=-Xmx2048m
 export JVM_OPTION="-Dfile.encoding=UTF-8 -Dserver.port=24119"

 do_start()
 {
         DAEMON_PID=`ps -ef | grep $DAEMON_NAME | grep java | awk '{print $2}'`
         if [ "${DAEMON_PID}" = "" ]
         then
                                 for jar in `find $DAEMON_HOME/lib -type d`
                                 do
                                      #echo $jar
                                      CLP=$CLP:$jar/*
                                 done

                 echo "$JAVA $XMS $XMX $JVM_OPTION -DNAME=$DAEMON_NAME -jar $MAIN &"
                 cd $DAEMON_HOME

                 nohup $JAVA $XMS $XMX $JVM_OPTION -DNAME=$DAEMON_NAME -jar $MAIN 1> /dev/null 2>&1 &
                 #nohup $JAVA $XMS $XMX $JVM_OPTION -DNAME=$DAEMON_NAME -jar $MAIN &
                 echo "$SYSDP_NAME has been successfully started."
         else
                 echo "$DAEMON_NAME already running."
         fi
 }

 do_stop()
 {
         DAEMON_PID=`ps -ef | grep $DAEMON_NAME | grep java | awk '{print $2}'`
         if [ "$DAEMON_PID" != "" ]
         then
                 kill $DAEMON_PID
                 echo "$DAEMON_NAME has been successfully stop. PID=$DAEMON_PID"
         else
                 echo "$DAEMON_NAME is not running."
         fi
 }

 case "$1" in
         start)
                 echo "$DAEMON_NAME start..."
                 do_start
 ;;
         stop)
                 echo "$DAEMON_NAME stopping..."
                 do_stop
 ;;
         restart)
                 $0 stop
                 $0 start
 ;;
         *)
         echo "Usage: $0 {start|stop|restart}"
         exit 1
 ;;
 esac

 exit 0
