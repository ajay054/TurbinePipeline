import os
from pipeline import ingest_data, clean_data, calculate_summary_statistics, detect_anomalies, save_results

# directories
data_dir = "./Data" 
output_dir = "./output"  
os.makedirs(output_dir, exist_ok=True)

# Main pipeline
def main():
    try:
        # Ingest Data
        raw_data = ingest_data(data_dir)

        # Clean Data
        cleaned_data = clean_data(raw_data)

        # Calculate Summary Statistics
        summary_stats = calculate_summary_statistics(cleaned_data)

        # Detect Anomalies
        anomalies = detect_anomalies(cleaned_data)

        # Step 5: Save Results
        save_results(cleaned_data, summary_stats, anomalies, output_dir)

        print("Pipeline executed successfully. Outputs are in the 'output' folder.")
    except Exception as e:
        print(f"Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()
