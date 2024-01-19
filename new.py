import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have already loaded the CSV file into a DataFrame
df = pd.read_csv("final_version.csv")

# Extract the month columns
month_columns = df.columns[2:14]

# Sum up the total milliseconds played for each month
total_ms_per_month = df[month_columns].sum()

# Convert the total milliseconds to minutes
total_minutes_per_month = total_ms_per_month / 60000  # Convert milliseconds to minutes

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=total_minutes_per_month.index, y=total_minutes_per_month.values, palette="viridis")
plt.title("Total Monthly Play Counts (in Minutes)")
plt.xlabel("Month")
plt.ylabel("Minutes Played")
plt.show()
