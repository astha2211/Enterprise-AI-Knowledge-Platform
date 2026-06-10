from pyspark.sql import SparkSession
import pandas as pd
import os

# Create Spark Session
spark = SparkSession.builder \
    .appName("GoldLayer") \
    .getOrCreate()

# Read Silver Layer
df = spark.read.csv(
    "data/silver/silver_data.csv",
    header=True,
    inferSchema=True
)

print("\n=== Silver Data Loaded ===\n")
df.show(10, truncate=False)

# Department-wise Analytics
gold_df = df.groupBy("department").count()

print("\n=== Department Analytics ===\n")
gold_df.show(truncate=False)

# Create Gold Folder
os.makedirs("data/gold", exist_ok=True)

# Save using Pandas
gold_pd = gold_df.toPandas()

gold_pd.to_csv(
    "data/gold/department_analytics.csv",
    index=False
)

print("\nGold Layer Created Successfully!")
print("Saved to: data/gold/department_analytics.csv")

spark.stop()