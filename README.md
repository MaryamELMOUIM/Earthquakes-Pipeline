# Earthquake Data Pipeline and Visualization

## Project Overview:

**Project Description:**
The project focuses on creating a comprehensive data solution for earthquake information. It encompasses two main phases: an ETL (Extract, Transform, Load) data pipeline and data visualization. The goal is to collect real-time earthquake data, process it using PySpark, store it in MongoDB, and present meaningful insights through visualizations.

## Project Phases:

### Phase One: ETL Data Pipeline
   - **Objective:** Develop a robust ETL pipeline to collect, process, and store live earthquake data.
   - **Key Components:**
     - Web Scraper (`web_scraper.py`): Extracts earthquake data through web scraping.
     - Data Processor (`data_processor.py`): Utilizes PySpark for data cleaning and transformation.
     - MongoDB Utility (`mongo_util.py`): Manages connections and data interactions with MongoDB.
     - Apache Airflow DAG (`airflow_dag.py`): Orchestrates and schedules tasks in the ETL workflow.
     ![USGS Earthquakes Feed - GeoJSON (2)](https://github.com/MaryamELMOUIM/Earthquakes_DataViz_BOUMAZZOURH_ELMOUIM/assets/152428007/d2c73c5b-3961-46be-afaf-fd5d79a8178b)



### Phase Two: Data Visualization
   - **Objective:** Visualize processed earthquake data to derive meaningful insights.
   - **Visualization Tool:**
     - **Tableau:**
        - Pros: Integrates seamlessly with processed data, widely used for data visualization.
        - Cons: May require a learning curve.
![image](https://github.com/user-attachments/assets/232653ce-ca57-4b51-8115-5b08a20bbec4)

![image](https://github.com/user-attachments/assets/51606bc4-5e59-42ea-b09d-73cdd0fdb379)


## Project Objectives:

1. **Collect Real-Time Earthquake Data:**
   - Implement a web scraper to gather live earthquake data from a reliable source.

2. **ETL Processing with PySpark:**
   - Develop a PySpark-based data processor to clean, transform, and structure the collected data.

3. **Efficient Storage with MongoDB:**
   - Utilize MongoDB for storing processed earthquake data, ensuring scalability and quick retrieval.

4. **Automated Workflow with Apache Airflow:**
   - Design an Apache Airflow DAG to automate and schedule the execution of ETL tasks.

5. **Meaningful Data Visualization:**
   - Leverage Tableau for creating insightful and interactive visualizations.

## Technologies Used:

1. **Web Scraping:**
   - Python, requests library.

2. **Data Processing:**
   - PySpark for efficient big data processing.

3. **Database:**
   - MongoDB as the NoSQL database for storing processed data.

4. **Workflow Orchestration:**
   - Apache Airflow for task automation and scheduling.

5. **Data Visualization:**
   - Tableau for creating insightful and interactive visualizations.

