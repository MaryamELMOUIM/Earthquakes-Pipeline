# Earthquake Data Processing Pipeline

## Project Overview

The Earthquake Data Processing Pipeline is a comprehensive data engineering project designed to collect, process, and store earthquake data obtained from the USGS Earthquake Hazards Program. The pipeline automates the workflow, ensuring a seamless and efficient process from data retrieval to storage.
![USGS Earthquakes Feed - GeoJSON (2)](https://github.com/MaryamELMOUIM/Earthquakes_DataViz_BOUMAZZOURH_ELMOUIM/assets/152428007/d31324c9-dd26-44f0-8054-c62e683c48c6)


## Components

### 1. Web Scraper (web_scraper.py)

- Retrieves earthquake data from the USGS GeoJSON feed (`all_month.geojson`).
- Extracts relevant information such as earthquake magnitude, location, time, and coordinates.
- Prepares the data for further processing.

### 2. Data Processor (data_processor.py)

- Ingests processed earthquake data into a Spark DataFrame using PySpark.
- Tasks include filtering earthquakes with a magnitude greater than 2.0, handling missing values, and converting data types for consistency.
- Optimizes the dataset by transforming geo-coordinates and dropping unnecessary columns.

### 3. MongoDB Utility (mongo_util.py)

- Provides utility functions for interacting with MongoDB.
- Includes functions to establish a Spark session, create a MongoDB client, load data from MongoDB into a Spark DataFrame, and save a Spark DataFrame back to MongoDB.

### 4. Airflow DAG (airflow_dag.py)

- Orchestrates the data pipeline using Apache Airflow.
- Defines tasks for web scraping (`web_scraper`) and data processing (`data_processor`).
- Task dependencies ensure web scraping is completed before data processing begins.

### 5. Configuration (config.py)

- Centralized configuration details, such as MongoDB connection parameters and other project-specific settings.

### 6. Requirements (requirements.txt)

- Lists dependencies required for the project.
