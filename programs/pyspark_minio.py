from pyspark.sql import SparkSession
# Create a SparkSession
#/Users/ramj/tvr-works/gh/venkataramant/local-data-lake/lib/hive_client_jars/
spark = SparkSession.builder \
        .master("spark://tvr-playbook.local:7077") \
        .config("fs.s3a.access.key", "minio_access_key")\
        .config("fs.s3a.secret.key", "minio_secret_key") \
        .config("fs.s3a.endpoint", "http://localhost:19000")\
        .config("fs.s3a.path.style.access", "true") \
        .config("fs.s3a.connection.ssl.enabled", "false") \
        .config("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("fs.s3a.connection.ssl.enabled", "false") \
        .config("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
        .config("spark.jars","./lib/hive_aux_jars/aws-core-2.27.2.jar,./lib/hive_aux_jars/hadoop-aws-3.3.3.jar,./lib/hive_aux_jars/aws-java-sdk-bundle-1.12.767.jar,./lib/hive_aux_jars/hadoop-common-3.3.3.jar")\
        .getOrCreate()
sc = spark.sparkContext
df = spark.read.text("s3a://tvr/big.txt")
df.show()