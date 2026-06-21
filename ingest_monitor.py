# ==============================================================================
# MODULE: Dynamic Ingestion Monitor
# DESCRIPTION: Dynamically parses JSON configurations with error handling
# ==============================================================================

import json
import os

CONFIG_FILE = "pipeline_config.json"

# 1. Resilient File Loading (Using try-except blocks)
try:
    print(f"[INFO] Attempting to read runtime configuration: {CONFIG_FILE}")
    
    with open(CONFIG_FILE, "r") as file:
        # Load parsing engine converting JSON to a Python Dictionary
        config_data = json.load(file)
        
    print("[SUCCESS] Configuration parsed into runtime memory.")

    # 2. Extracting Values from Python Dictionary via Keys
    service = config_data["target_cloud_service"]
    delay = config_data["ingestion_delay_minutes"]
    rate = config_data["compute_cost_per_hour"]

    # 3. Core Transformation Logic
    operational_loss_usd = (delay / 60) * rate

    # 4. Telemetry Log Output
    print("\n--- [SENTINEL FLOW: SYSTEM TELEMETRY] ---")
    print(f"Target Resource : {service}")
    print(f"Pipeline Delay  : {delay} minutes")
    print(f"Calculated Cost : ${round(operational_loss_usd, 4)} USD")
    print("-----------------------------------------\n")

except FileNotFoundError:
    print(f"[CRITICAL ERROR] Failed execution: '{CONFIG_FILE}' missing from directory.")
except json.JSONDecodeError:
    print(f"[CRITICAL ERROR] Failed execution: '{CONFIG_FILE}' is malformed or corrupted.")