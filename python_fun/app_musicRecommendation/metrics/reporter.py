from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import collect_list, concat_ws, countDistinct, lag
from pyspark.sql.functions import max as max_
from pyspark.sql.functions import min as min_
from pyspark.sql.functions import round as round_
from pyspark.sql.functions import sum as sum_
from pyspark.sql.functions import unix_timestamp
from pyspark.sql.types import IntegerType, LongType
from pyspark.sql.window import Window


def distinct_songs_per_user(df: DataFrame) -> DataFrame:
    return df.groupBy("userid").agg(countDistinct("track-name").alias('DistinctSongs'))


def top_100_songs(df: DataFrame) -> DataFrame:
    return df.groupBy("artist-name", "track-name").count()


def top_10_sessions(df: DataFrame, duration: int) -> DataFrame:

    w = Window.partitionBy("userid").orderBy("timestamp")

    df = df.withColumn("isDiff", (df["timestamp"].cast(LongType(
    )) - lag(df["timestamp"].cast(LongType()), 1).over(w) >= (duration * 60)).cast(IntegerType()))

    sessionid = sum_(df["isDiff"]).over(w).alias("sessionid")

    df = df.select("*", sessionid).groupBy("userid", "sessionid").agg(
        min_("timestamp").alias("start_session"),
        max_("timestamp").alias("end_session"),
        concat_ws("; ", collect_list(df["track-name"])).alias("track_list"))

    return df.withColumn("time_elapsed_minutes", round_(
        (unix_timestamp(df['end_session']) - unix_timestamp(df['start_session']))/60))
