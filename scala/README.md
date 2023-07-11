# Spark 2

### Configuration example with Spark 2.x.x and Cassandra 3.x:
```
$ vi /usr/local/spark-2.1.1/conf/spark-defaults.conf
     \__ spark.jars.packages datastax:spark-cassandra-connector:2.0.5-s_2.11

$ spark-shell
```


### References:

[https://jaceklaskowski.gitbooks.io/mastering-apache-spark](https://jaceklaskowski.gitbooks.io/mastering-apache-spark)
