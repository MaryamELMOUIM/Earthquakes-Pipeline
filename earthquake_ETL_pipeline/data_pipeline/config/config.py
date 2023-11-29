from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

class Config:
    # Set up the MongoDB connection details
    password = 'MAR@yam123'
    escaped_password = quote_plus(password)

    # Use escaped password in URI
    MONGO_URI = f"mongodb+srv://maryam_elmou:{escaped_password}@bigdata.zdq8pq6.mongodb.net/?retryWrites=true&w=majority"
    
    DATABASE_NAME = "weather_database"
    INPUT_COLLECTION = "all_month_earthquake"
    OUTPUT_COLLECTION = "processed_data"

    # Add other configuration parameters as needed
