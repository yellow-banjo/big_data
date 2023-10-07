Для развертывания standalone cluster Spark в командной строке были последовательно выполнены следующие команды:
1) ./sbin/start-master.sh
2) export SPARK_IDENT_STRING=worker1 ; ./sbin/start-worker.sh spark://DESKTOP-5R90GJV.:7077
3) export SPARK_IDENT_STRING=worker2 ; ./sbin/start-worker.sh spark://DESKTOP-5R90GJV.:7077
