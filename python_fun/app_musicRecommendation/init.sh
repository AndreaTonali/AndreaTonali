
if [ -z "${SPARK_HOME}" ]; then
    echo "Please setup Spark"
    exit 1
else
    echo "start music-recommendation"
    python app.py
fi