# process_data.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataJoin").getOrCreate()

# Read CSVs
employees = spark.read.csv("employees.csv", header=True, inferSchema=True)
salaries = spark.read.csv("salaries.csv", header=True, inferSchema=True)

# Join and save
joined_df = employees.join(salaries, "id")
joined_df.write.mode("overwrite").csv("output/joined_data")
print("Data processed successfully")
