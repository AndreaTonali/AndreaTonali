from pyspark.sql.dataframe import DataFrame


def assign_headers(df: DataFrame) -> DataFrame:
    formatted_headers = ["userid", "timestamp", "musicbrainz-artist-id",
                         "artist-name", "musicbrainz-track-id", "track-name"]
    old_headers = [c for c in df.columns]
    for old_header, formatted_header in zip(old_headers, formatted_headers):
        df = df.withColumnRenamed(old_header, formatted_header)
    return df
