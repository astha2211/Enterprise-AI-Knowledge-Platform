from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, trim
import pandas as pd
import os

# Create Spark Session
spark = SparkSession.builder \
    .appName("SilverLayer") \
    .getOrCreate()

# Read Bronze Layer
df = spark.read.csv(
    "data/bronze/knowledge_base.csv",
    header=True,
    inferSchema=True
)

# Data Cleaning & Transformation
silver_df = (
    df.dropDuplicates()
      .na.drop()
      .withColumn("department", trim(lower(df.department)))
)

print("\n=== Silver Layer Preview ===\n")
silver_df.show(50, truncate=False)

print("\n=== Schema ===\n")
silver_df.printSchema()

# Create output folder if not exists
os.makedirs("data/silver", exist_ok=True)

# Convert Spark DataFrame to Pandas
silver_pd = silver_df.toPandas()

# Save cleaned data
silver_pd.to_csv(
    "data/silver/silver_data.csv",
    index=False
)

print("\nSilver Layer Created Successfully!")
print("Saved to: data/silver/silver_data.csv")

# Stop Spark Session
spark.stop()