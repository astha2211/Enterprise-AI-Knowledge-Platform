from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BronzeLayer") \
    .getOrCreate()

df = spark.read.csv(
    "data/bronze/knowledge_base.csv",
    header=True,
    inferSchema=True
)

print("\nDataset Preview:\n")
df.show(10, truncate=False) 

print("\nSchema:\n")
df.printSchema()

spark.stop()

#df.show(df.count(), truncate=False) to display all rws