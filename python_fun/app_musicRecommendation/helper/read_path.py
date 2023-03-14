from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import to_timestamp
from pyspark.sql.session import SparkSession
from pyspark.sql.utils import AnalysisException
import logging

from helper.utils import assign_headers


class Reader:

    def __init__(self, spark: SparkSession):
        self.spark = spark
        self.logger = logging.getLogger(__name__)

    def read_userid_timestamp_data(self, path: str) -> DataFrame:
        try:
            df = self.spark.read.csv(path, sep=r'\t', header=False)
            df = assign_headers(df)
            df = df.withColumn("timestamp", to_timestamp("timestamp"))
            return df
        except AnalysisException as e:
            self.logger.info(f"Missing dataset: {e}")
