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

# Drop rows where parsing failed or glucose is missing
df = df.dropna(subset=["Device Timestamp", "Historic Glucose mg/dL"])

# Create a date-only column (bucket by day)
df["date"] = df["Device Timestamp"].dt.date

# Group by date and compute average glucose
daily_avg = (
    df.groupby("date")["Historic Glucose mg/dL"]
    .mean()
    .reset_index()
)

# Rename columns to match desired output
daily_avg = daily_avg.rename(columns={
    "date": "Device Timestamp",
    "Historic Glucose mg/dL": "average_glucose"
})

# Save to CSV
daily_avg.to_csv(output_csv, index=False)

print(f"Saved daily averages to {output_csv}")
