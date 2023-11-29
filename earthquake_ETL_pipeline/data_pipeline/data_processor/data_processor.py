from pyspark.sql.functions import col
from pyspark.sql.types import DecimalType, TimestampType
from storage_loader.mongo_util import load_data_from_mongo, save_data_to_mongo, get_spark_session

def process_data(spark):
    # MongoDB connection details
    mongo_uri = Config.MONGO_URI
    database = Config.DATABASE_NAME
    input_collection = Config.INPUT_COLLECTION
    output_collection = Config.OUTPUT_COLLECTION

    # Load data from MongoDB
    df = load_data_from_mongo(spark, mongo_uri, database, input_collection)

    # Perform data processing
    processed_df = (
        df
        .filter(col("mag") > 2.0)
        .dropDuplicates()
        .na.drop()
        .withColumn("mag", col("mag").cast(DecimalType(10, 8)))
        .withColumn("time", col("time").cast(TimestampType()))
        .withColumn("longitude", col("coordinates")[0].cast(DecimalType(18, 14)))
        .withColumn("latitude", col("coordinates")[1].cast(DecimalType(18, 14)))
        .withColumn("depth", col("coordinates")[2].cast(DecimalType(18, 14)))
        .drop("coordinates")
    )

    # Save the processed data back to MongoDB
    save_data_to_mongo(processed_df, mongo_uri, database, output_collection, mode="overwrite")

if __name__ == "__main__":
    # Initialize Spark session
    spark = get_spark_session()

    # Process data
    process_data(spark)

    # Stop Spark session
    spark.stop()
