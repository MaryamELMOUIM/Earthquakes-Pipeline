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

### Phase Two: Data Visualization
   - **Objective:** Visualize processed earthquake data to derive meaningful insights.
   - **Options:**
     1. **Informative Dashboard:**
        - Pros: Interactive, user-friendly, customizable.
        - Cons: May require third-party dashboarding tools.
     2. **Flask Web Dashboard:**
        - Pros: Customizable, integrates well with Python visualization libraries.
        - Cons: Requires additional development effort.

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
   - Visualize earthquake data through either an informative dashboard or a Flask web dashboard.

## Technologies Used:

1. **Web Scraping:**
   - Python, requests library.

2. **Data Processing:**
   - PySpark for efficient big data processing.

3. **Database:**
   - MongoDB as the NoSQL database for storing processed data.

4. **Workflow Orchestration:**
   - Apache Airflow for task automation and scheduling.

5. **Data Visualization (Options):**
   - Informative Dashboard: Tableau, Power BI, or similar tools.
   - Flask Web Dashboard: Flask, Python visualization libraries (e.g., Plotly, Bokeh).

## Next Steps:

1. Complete the implementation of the ETL data pipeline.
2. Choose the preferred data visualization option (dashboard or Flask web dashboard).
3. Implement the selected visualization approach, showcasing insights from the earthquake data.

By successfully executing both phases, the project aims to establish an end-to-end solution for earthquake data, combining data processing efficiency with insightful visualizations.
