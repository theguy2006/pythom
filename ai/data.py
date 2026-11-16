
import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Aracati weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=-4.56&longitude=-37.77&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=America/Fortaleza"

response = requests.get(url)
data = response.json()

# Extract daily data
daily_data = data['daily']

# Create DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert dates
df['date'] = pd.to_datetime(df['date'])

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Aracati Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()

# Create data folder
if not os.path.exists('data'):
    os.makedirs('data')

# Save graph
plt.savefig('data/aracati_weather.png')
plt.show()

# Save to CSV
df.to_csv('data/aracati_weather.csv', index=False)

print("Data saved to data/aracati_weather.csv")
print("Graph saved to data/aracati_weather.png")
