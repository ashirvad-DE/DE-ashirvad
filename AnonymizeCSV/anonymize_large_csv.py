from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2

def anonymize_large_csv(input_file, output_file):
    spark = SparkSession.builder \
        .appName("Anonymize CSV") \
        .getOrCreate()

    df = spark.read.csv(input_file, header=True)

    # Anonymize the columns
    df = df.withColumn("first_name", sha2(df.first_name, 256)) \
           .withColumn("last_name", sha2(df.last_name, 256)) \
           .withColumn("address", sha2(df.address, 256))

    df.write.csv(output_file, header=True)
    spark.stop()

if __name__ == "__main__":
    anonymize_large_csv('data/sample_data.csv', 'data/anonymized_data_large')
