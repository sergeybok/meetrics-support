import pandas as pd

# Input / output paths
input_csv = "SergiyBokhnyak_glucose_4-3-2026.csv"
output_csv = "daily_average_glucose.csv"

# Read CSV
df = pd.read_csv(input_csv)

# Parse datetime
df["Device Timestamp"] = pd.to_datetime(
    df["Device Timestamp"],
    format="%m-%d-%Y %I:%M %p",
    errors="coerce"
)

# Drop invalid rows
df = df.dropna(subset=["Device Timestamp", "Historic Glucose mg/dL"])

# Bucket by day
df["date"] = df["Device Timestamp"].dt.date

# Group and compute metrics
daily_stats = (
    df.groupby("date")["Historic Glucose mg/dL"]
    .agg(
        average_glucose="mean",
        pct_75=lambda x: x.quantile(0.75)
    )
    .reset_index()
)

# Rename columns
daily_stats = daily_stats.rename(columns={
    "date": "Device Timestamp",
    "pct_75": "75th_pct_glucose"
})

# Optional: sort by date
daily_stats = daily_stats.sort_values("Device Timestamp")

# Save
daily_stats.to_csv(output_csv, index=False)

print(f"Saved daily stats to {output_csv}")
