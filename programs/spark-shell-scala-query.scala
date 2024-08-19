 import org.apache.spark.sql.{Row, SaveMode, SparkSession}

sc.hadoopConfiguration.set("fs.s3a.endpoint", "http://127.0.0.1:19000");
sc.hadoopConfiguration.set("fs.s3a.access.key","minio_access_key");
sc.hadoopConfiguration.set("fs.s3a.secret.key","minio_secret_key");


val spark = SparkSession.builder().appName("SparkHiveTest").confg(sc.getConf).config("hive.metastore.uris", "thrift://localhost:9083").config("spark.sql.warehouse.dir", "s3a://hive/warehouse").enableHiveSupport().getOrCreate()

import org.apache.spark.sql.{Row, SaveMode, SparkSession}

sc.hadoopConfiguration.set("fs.s3a.endpoint", "http://127.0.0.1:19000");
sc.hadoopConfiguration.set("fs.s3a.access.key","minio_access_key");
sc.hadoopConfiguration.set("fs.s3a.secret.key","minio_secret_key");
sc.setLogLevel("Debug")
val sparkSession = SparkSession.builder.appName("SparkHiveTest").config(sc.getConf).config("hive.metastore.uris", "thrift://localhost:9083").config("spark.sql.warehouse.dir", "s3a://hive/warehouse").enableHiveSupport().getOrCreate()
sparkSession.sql("show databases").show()
sparkSession.sql("show tables in mydatabase").show()
sparkSession.sql("select * from mydatabase.src").show()
sparkSession.sql("select count(*) from mydatabase.src").show()
sparkSession.sql("show tables in mydatabase").show()