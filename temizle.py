import pandas as pd
import json
from unidecode import unidecode  # Import unidecode

# Assuming the file paths for your streaming history files are as follows
file_paths = ["StreamingHistory_music_0.json", "StreamingHistory_music_1.json", "StreamingHistory_music_2.json"]

# Initialize an empty list to store data from each file
data = []

# Loop through each file and read the data
for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        streaming_data = json.load(file)
        data.extend(streaming_data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Group by artistName and trackName, summing the msPlayed for each track
df_grouped = df.groupby(['artistName', 'trackName']).agg({'msPlayed': 'sum'}).reset_index()

# Print the resulting DataFrame
print(df_grouped)
df_grouped.to_csv('music.csv', index=False)