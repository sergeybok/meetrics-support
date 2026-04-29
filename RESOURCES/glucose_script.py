import pandas as pd

# Input / output paths
input_csv = "SergiyBokhnyak_glucose_4-29-2026.csv"
output_csv = "daily_average_glucose.csv"
insulin_output_csv = "rapid_acting_insulin.csv"

# Read CSV (row 0 is metadata, row 1 is the real header)
df = pd.read_csv(input_csv, skiprows=1, low_memory=False)

# Parse datetime
df["Device Timestamp"] = pd.to_datetime(
    df["Device Timestamp"],
    format="%m-%d-%Y %I:%M %p",
    errors="coerce"
)

# --- Daily average glucose ---
glucose_df = df.dropna(subset=["Device Timestamp", "Historic Glucose mg/dL"]).copy()
glucose_df["date"] = glucose_df["Device Timestamp"].dt.date

daily_stats = (
    glucose_df.groupby("date")["Historic Glucose mg/dL"]
    .agg(
        average_glucose="mean",
        pct_75=lambda x: x.quantile(0.75)
    )
    .reset_index()
)

daily_stats = daily_stats.rename(columns={
    "date": "Device Timestamp",
    "pct_75": "75th_pct_glucose"
})

daily_stats = daily_stats.sort_values("Device Timestamp")
daily_stats.to_csv(output_csv, index=False)
print(f"Saved daily stats to {output_csv}")

# --- Rapid-acting insulin (non-null, with accurate timestamps) ---
insulin_df = df.dropna(subset=["Device Timestamp", "Rapid-Acting Insulin (units)"]).copy()
insulin_df = insulin_df[["Device Timestamp", "Rapid-Acting Insulin (units)"]].sort_values("Device Timestamp")
insulin_df.to_csv(insulin_output_csv, index=False)
print(f"Saved rapid-acting insulin to {insulin_output_csv}")
