import requests
from pymongo import MongoClient
from urllib.parse import quote_plus
from config.config import Config

def scrape_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    response = requests.get(url)
    data = response.json()

    # Use configuration parameters for MongoDB connection
    uri = Config.MONGO_URI

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Access the specified collection or create it if it doesn't exist
    collection_name = Config.INPUT_COLLECTION
    collection = client[Config.DATABASE_NAME][collection_name]

    # Extract relevant fields from GeoJSON features
    cleaned_features = []
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']['coordinates']

        # Create a new feature with the desired structure
        new_feature = {
            'mag': properties['mag'],
            'place': properties['place'],
            'time': properties['time'],
            'coordinates': geometry,
            'id': feature['id'],
            # Add other desired properties here
        }

        # Append the modified feature to the new list
        cleaned_features.append(new_feature)

    # Insert the new data into the MongoDB collection
    collection.insert_many(cleaned_features)

# Uncomment the line below if you want to run the scraper function when this script is executed directly
# scrape_earthquake_data()

