Wind Turbine Data Processing Pipeline
Overview
This project is a scalable and testable data processing pipeline designed for a renewable energy company that operates a farm of wind turbines. The pipeline processes raw data collected from turbines, cleans it, calculates summary statistics, identifies anomalies, and stores the processed data for further analysis.

The pipeline is written in Python and is structured to handle daily data updates efficiently.

Features
Data Ingestion:

Combines multiple raw CSV files into a single dataset.
Each file corresponds to a group of turbines.
Data Cleaning:

Handles missing values by imputing with the column mean.
Removes outliers using a z-score threshold (2 standard deviations).
Summary Statistics:

Calculates minimum, maximum, and average power output for each turbine.
Anomaly Detection:

Identifies turbines with power output significantly deviating from their mean (beyond 2 standard deviations).
Results Storage:

Saves the cleaned data, summary statistics, and anomalies as CSV files.
Generates a bar chart visualization of the summary statistics.
Project Structure

project/
├── Data/              
├── output/            
├── main.py            
├── pipeline.py        
└── README.md   

How to Run the Project

1. Prerequisites
Python 3.6 or higher
Required libraries:

pip install pandas matplotlib

2. Setup
Place all raw CSV files in the Data/ folder.
Ensure the output/ folder exists (the script will create it automatically if not).

4. Execute the Pipeline
Run the main.py script:

main.py
Outputs
After running the pipeline, you will find the following files in the output/ directory:

Cleaned Data: cleaned_data.csv - Data after cleaning and outlier removal.

Summary Statistics: summary_statistics.csv - Min, max, and average power outputs for each turbine.

Anomalies: anomalies.csv - Turbines with power output anomalies.

Visualisation: summary_statistics.png - Bar chart of turbine summary statistics.
Customisation


To update or add more turbines, simply place new CSV files in the Data/ folder.

To adjust the anomaly detection threshold, modify the z-score condition in the pipeline.py file.
Example CSV File Structure

Each CSV file should follow this format:

timestamp	turbine_id	wind_speed	wind_direction	power_output
2023-01-01 00:00:00	1	12.4	180	2.5
2023-01-01 01:00:00	2	10.2	200	1.9
turbine_id: Unique ID for each turbine.
power_output: Power generated in megawatts (MW).
timestamp: Date and time of measurement.


Scalability
The pipeline is designed to handle daily updates seamlessly by ingesting new data from the Data/ folder.
New turbines or additional data files can be added without modifying the code.
