from pyhive import hive
conn = hive.Connection(host="localhost",port=10000)
cursor = conn.cursor()
cursor.execute("Select * from nyc.taxis")
for result in cursor.fetchall():
   print(result)

import pandas as pd
df = pd.read_sql("Select * from nyc.taxis", conn)
print(df.to_json())