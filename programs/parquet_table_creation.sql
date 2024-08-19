 create  table mydatabase.parquet_data(dest_ip string,dest_port int,isBoolean boolean, mydate timestamp, difficult_filed2 string, nested_field STRUCT<field_1:STRING, field_2:STRING>) PARTITIONED BY (year int, month int, day int)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
tblproperties ("parquet.compress"="SNAPPY");


insert into parquet_data values('10.0.0.1',9090,true,cast('2021-03-14 02:01:03.118' as timestamp),'my filed2' , NAMED_STRUCT( 'field_1','v1','field_2','v2'),2023,10,5)

