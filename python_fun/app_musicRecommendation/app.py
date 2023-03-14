import logging

from pyspark.sql.functions import desc

from helper.read_path import Reader
from metrics.reporter import distinct_songs_per_user, top_100_songs, top_10_sessions
from settings.settings import DATA_SOURCE, spark


def main() -> None:

    logger = logging.getLogger(__name__)

    reader = Reader(spark=spark)
    userid_timestamp = reader.read_userid_timestamp_data(DATA_SOURCE)

    logger.info(userid_timestamp.printSchema())
    
    dfa = distinct_songs_per_user(userid_timestamp).sort(desc('DistinctSongs'))
    logger.info(dfa.show(10))
    
    dfa.limit(10)\
       .repartition(1)\
       .write\
       .mode('overwrite')\
       .format("com.databricks.spark.csv")\
       .option("header", "true")\
       .save("SolutionA")
    
    dfb = top_100_songs(userid_timestamp).sort(desc('count'))
    logger.info(dfb.show(100))
    dfb.limit(100)\
       .repartition(1)\
       .write\
       .mode('overwrite')\
       .format("com.databricks.spark.csv")\
       .option("header", "true")\
       .save("SolutionB")

    dfc = top_10_sessions(userid_timestamp, 20).sort(desc("time_elapsed_minutes"))
    logger.info(dfc.show(10))
    dfc.limit(10)\
       .repartition(1)\
       .write\
       .mode('overwrite')\
       .format("com.databricks.spark.csv")\
       .option("header", "true")\
       .save("SolutionC")


if __name__ == '__main__':
    main()
