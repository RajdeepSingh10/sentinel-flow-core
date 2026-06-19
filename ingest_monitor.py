# ==============================================================================
# MODULE: Ingestion Monitor Baseline
# DESCRIPTION: Tracks operational states and core metrics for Sentinel Flow
# ==============================================================================

# 1. System Metadata (Data Types: Strings, Integers, Floats)
target_cloud_service = "Amazon_RDS_Cluster"  # String
ingestion_delay_minutes = 14                  # Integer
compute_cost_per_hour = 24.55                # Float

# 2. Operational Logic
# Convert minutes to hours fraction, then calculate compute cost impact
operational_loss_usd = (ingestion_delay_minutes / 60) * compute_cost_per_hour

# 3. Telemetry Output (Simulating a production log entry)
print("--- [SENTINEL FLOW: SYSTEM TELEMETRY] ---")
print(f"Target Resource : {target_cloud_service}")
print(f"Pipeline Delay  : {ingestion_delay_minutes} minutes")
print(f"Calculated Cost : ${round(operational_loss_usd, 4)} USD")
print("-----------------------------------------")