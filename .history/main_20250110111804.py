import os
from pipeline import ingest_data, clean_data, calculate_summary_statistics, detect_anomalies, save_results

# Define directories
data_dir = "./Data"  # Directory containing raw CSV files
output_dir = "./output"  # Directory to save processed data and results
os.makedirs(output_dir, exist_ok=True)

# Main pipeline
def main():
    try:
        # Step 1: Ingest Data
        raw_data = ingest_data(data_dir)

        # Step 2: Clean Data
        cleaned_data = clean_data(raw_data)

        # Step 3: Calculate Summary Statistics
        summary_stats = calculate_summary_statistics(cleaned_data)

        # Step 4: Detect Anomalies
        anomalies = detect_anomalies(cleaned_data)

        # Step 5: Save Results
        save_results(cleaned_data, summary_stats, anomalies, output_dir)

        print("Pipeline executed successfully. Outputs are in the 'output' folder.")
    except Exception as e:
        print(f"Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()
