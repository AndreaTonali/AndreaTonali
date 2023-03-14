from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .config("spark.driver.memory", "10g") \
    .config("spark.cores.max", "10") \
    .config("spark.executor.cores", "2") \
    .config("spark.executor.memory", "12g") \
    .config("spark.logConf", "true") \
    .getOrCreate()


DATA_SOURCE = "dataset/userid-timestamp-artid-artname-traid-traname.tsv"
