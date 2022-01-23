from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession \
            .builder \
            .getOrCreate()

    df = spark.read.csv((r"C:\Users\VIKAS\Desktop\Python\Spark-Programminng\data\sample.csv"))
    df.show()



