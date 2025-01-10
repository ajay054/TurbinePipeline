import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Data Ingestion
def ingest_data(data_dir):
    """Combine data from multiple CSV files."""
    all_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".csv")]
    data_frames = []
    for file in all_files:
        df = pd.read_csv(file)
        df['source_file'] = os.path.basename(file)  # Add a column to track source file
        data_frames.append(df)
    combined_data = pd.concat(data_frames, ignore_index=True)
    print("Data ingestion completed.")
    return combined_data

# Step 2: Data Cleaning
def clean_data(df):
    """Handle missing values and remove outliers."""
    # Ensure power_output is numeric
    df['power_output'] = pd.to_numeric(df['power_output'], errors='coerce')
    
    # Handle missing values by imputing with column mean
    df['power_output'].fillna(df['power_output'].mean(), inplace=True)
    
    # Remove outliers based on z-score
    mean = df['power_output'].mean()
    std_dev = df['power_output'].std()
    z_score = (df['power_output'] - mean) / std_dev
    df = df[np.abs(z_score) <= 2]  # Retain data within 2 standard deviations
    print("Data cleaning completed.")
    return df

# Step 3: Summary Statistics
def calculate_summary_statistics(df):
    """Calculate min, max, and average power output per turbine."""
    summary = df.groupby('turbine_id').agg(
        min_power=('power_output', 'min'),
        max_power=('power_output', 'max'),
        avg_power=('power_output', 'mean')
    ).reset_index()
    print("Summary statistics calculated.")
    return summary

# Step 4: Anomaly Detection
def detect_anomalies(df):
    """Identify turbines with outputs outside 2 standard deviations."""
    anomalies = df.groupby('turbine_id').apply(
        lambda group: group[np.abs(group['power_output'] - group['power_output'].mean()) > 2 * group['power_output'].std()]
    ).reset_index(drop=True)
    print("Anomalies detected.")
    return anomalies

# Step 5: Save Results
def save_results(cleaned_data, summary_stats, anomalies, output_dir):
    """Save processed data and visualizations."""
    # Save cleaned data
    cleaned_data.to_csv(os.path.join(output_dir, "cleaned_data.csv"), index=False)
    print("Cleaned data saved.")

    # Save summary statistics
    summary_stats.to_csv(os.path.join(output_dir, "summary_statistics.csv"), index=False)
    print("Summary statistics saved.")

    # Save anomalies
    anomalies.to_csv(os.path.join(output_dir, "anomalies.csv"), index=False)
    print("Anomalies saved.")

    # Visualization
    plt.figure(figsize=(10, 6))
    summary_stats.plot(x='turbine_id', y=['min_power', 'max_power', 'avg_power'], kind='bar')
    plt.title('Summary Statistics per Turbine')
    plt.savefig(os.path.join(output_dir, "summary_statistics.png"))
    print("Visualization saved.")
