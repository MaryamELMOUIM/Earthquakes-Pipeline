from pyspark.sql import SparkSession
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

def get_spark_session(app_name="EarthquakeDataProcessor"):
    """
    Get or create a Spark session with MongoDB Spark connector configuration.

    Parameters:
    - app_name (str): The name of the Spark application.

    Returns:
    SparkSession: The Spark session.
    """
    spark = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1")  # Specify the correct version
        .getOrCreate()
    )
    return spark

def get_mongo_client(mongo_uri, server_api_version='1'):
    """
    Get a MongoClient instance for MongoDB.

    Parameters:
    - mongo_uri (str): The MongoDB connection URI.
    - server_api_version (str): The MongoDB Server API version (default: '1').

    Returns:
    MongoClient: The MongoDB client instance.
    """
    return MongoClient(mongo_uri, server_api=ServerApi(server_api_version))

def load_data_from_mongo(spark, mongo_uri, database, collection):
    """
    Load data from MongoDB into a Spark DataFrame.

    Parameters:
    - spark (SparkSession): The Spark session.
    - mongo_uri (str): The MongoDB connection URI.
    - database (str): The MongoDB database name.
    - collection (str): The MongoDB collection name.

    Returns:
    DataFrame: The loaded Spark DataFrame.
    """
    # Load data from MongoDB into Spark DataFrame
    return (
        spark
        .read
        .format("com.mongodb.spark.sql.DefaultSource")
        .option("uri", mongo_uri)
        .option("database", database)
        .option("collection", collection)
        .load()
    )

def save_data_to_mongo(dataframe, mongo_uri, database, collection, mode="overwrite"):
    """
    Save a Spark DataFrame to MongoDB.

    Parameters:
    - dataframe (DataFrame): The Spark DataFrame to be saved.
    - mongo_uri (str): The MongoDB connection URI.
    - database (str): The MongoDB database name.
    - collection (str): The MongoDB collection name.
    - mode (str): The mode for saving data (default: "overwrite").

    Returns:
    None
    """
    (
        dataframe
        .write
        .format("com.mongodb.spark.sql.DefaultSource")
        .option("uri", mongo_uri)
        .option("database", database)
        .option("collection", collection)
        .mode(mode)
        .save()
    )
