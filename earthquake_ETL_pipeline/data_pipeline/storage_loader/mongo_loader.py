from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
from pyspark.sql import DataFrame

def load_to_mongo(dataframe: DataFrame, mongo_uri: str, database: str, collection: str, mode: str = "overwrite"):
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
    # Create a MongoClient instance
    client = MongoClient(mongo_uri)

    # Access the specified collection or create it if it doesn't exist
    collection = client[database][collection]

    # Convert Spark DataFrame to Pandas DataFrame
    pandas_df = dataframe.toPandas()

    # Convert Pandas DataFrame to list of dictionaries
    data_list = pandas_df.to_dict(orient='records')

    # Insert the new data into the MongoDB collection
    if mode == "overwrite":
        collection.delete_many({})  # Delete existing documents in the collection before inserting
    collection.insert_many(data_list)
