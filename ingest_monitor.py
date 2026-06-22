# ==============================================================================
# MODULE: Batch Ingestion & Metric Aggregator
# DESCRIPTION: Iterates over log streams and calculates aggregated risk metrics
# ==============================================================================

import json

DATA_STREAM_FILE = "batch_infrastructure_logs.json"

try:
    print(f"[INFO] Accessing data stream pipeline from: {DATA_STREAM_FILE}")
    
    with open(DATA_STREAM_FILE, "r") as file:
        # Load parses the JSON array into a Python List of Dictionaries
        log_batch = json.load(file)
    
    print(f"[SUCCESS] Ingested a batch of {len(log_batch)} infrastructure records.")
    print("\n================== PIPELINE EXECUTION REPORT ==================")
    
    # Track the total cost impact of all broken pipelines combined
    cumulative_loss_usd = 0.0

    # The Engine: Loop through each individual log dictionary inside the list
    for log in log_batch:
        service = log["target_cloud_service"]
        delay = log["ingestion_delay_minutes"]
        rate = log["compute_cost_per_hour"]
        
        # Calculate impact for this specific service
        loss_usd = (delay / 60) * rate
        
        # Accumulate the loss into our running total metric
        cumulative_loss_usd = cumulative_loss_usd + loss_usd
        
        # Print status for this specific resource line-item
        print(f"-> Resource: {service:<30} | Loss: ${round(loss_usd, 2):<6} USD")

    print("===============================================================")
    print(f"TOTAL BATCH FINANCIAL EXPOSURE: ${round(cumulative_loss_usd, 2)} USD")
    print("===============================================================\n")

except FileNotFoundError:
    print(f"[CRITICAL ERROR] Stream file '{DATA_STREAM_FILE}' unavailable.")