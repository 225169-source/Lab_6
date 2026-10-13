import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dataset (16 entries including 1 duplicate)
data = {
    'Date': [
        '2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04', '2023-09-05',
        '2023-09-06', '2023-09-07', '2023-09-08', '2023-09-09', '2023-09-10',
        '2023-09-11', '2023-09-12', '2023-09-13', '2023-09-14', '2023-09-15',
        '2023-09-15'
    ],
    'City': [
        ' Islamabad', 'ISLAMABAD', 'islamabad ', ' Islamabad', 'Islamabad',
        ' Islamabad', 'ISLAMABAD', 'islamabad ', ' Islamabad', 'Islamabad',
        ' Islamabad', 'ISLAMABAD', 'islamabad ', ' Islamabad', 'Islamabad',
        'Islamabad'
    ],
    'Temperature': [
        '32C', '34C', '30C', '28C', '29C',
        '31C', '35C', '33C', '27C', '26C',
        '30C', '32C', '34C', '29C', '28C',
        '28C'
    ],
    'Humidity': [
        50.0, 45.0, None, 65.0, 60.0,
        52.0, None, 48.0, 70.0, 75.0,
        58.0, None, 42.0, 62.0, 68.0,
        68.0
    ],
    'Condition': [
        'sunny', ' Sunny', 'CLOUDY ', 'Rainy', 'sunny',
        'Sunny ', 'sunny', 'CLOUDY', ' Rainy', 'cloudy',
        'Sunny', 'cloudy', 'sunny', 'Rainy', 'cloudy',
        'cloudy'
    ]
}

df = pd.DataFrame(data)

# 2. Cleaning, Deduplication & Imputation
df['City'] = df['City'].str.strip().str.title()
df['Condition'] = df['Condition'].str.strip().str.title()
df['Temperature'] = pd.to_numeric(df['Temperature'].str.replace('C', '', regex=False))
df['Date'] = pd.to_datetime(df['Date'])

df = df.drop_duplicates()
df['Humidity'] = df['Humidity'].fillna(df['Humidity'].median())

# One-Hot Encoding
condition_dummies = pd.get_dummies(df['Condition'], prefix='Condition', dtype=int)

print("Cleaned Weather DataFrame:")
print(df)
print("\nCorrelation between Temperature & Humidity:", df['Temperature'].corr(df['Humidity']))

# 3. 2x2 Dashboard
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Weather Overview', fontsize=16, fontweight='bold')

# Line plot: Temperature over time
axs[0, 0].plot(df['Date'], df['Temperature'], marker='o', color='crimson', linewidth=2)
axs[0, 0].set_title('Temperature Over Time')
axs[0, 0].set_xlabel('Date')
axs[0, 0].set_ylabel('Temperature (°C)')
axs[0, 0].tick_params(axis='x', rotation=45)
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# Scatter plot: Temperature vs Humidity
axs[0, 1].scatter(df['Temperature'], df['Humidity'], color='blue', alpha=0.7, edgecolors='black')
axs[0, 1].set_title('Temperature vs. Humidity')
axs[0, 1].set_xlabel('Temperature (°C)')
axs[0, 1].set_ylabel('Humidity (%)')
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# Pie chart: Condition distribution
cond_counts = df['Condition'].value_counts()
axs[1, 0].pie(cond_counts.values, labels=cond_counts.index, autopct='%1.1f%%', startangle=90)
axs[1, 0].set_title('Condition Share')

# Histogram: Temperature distribution
axs[1, 1].hist(df['Temperature'], bins=5, color='orange', edgecolor='black')
axs[1, 1].set_title('Temperature Distribution')
axs[1, 1].set_xlabel('Temperature (°C)')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# 4. Save Image directly in script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(script_dir, 'weather_dashboard.png'), dpi=300)
plt.show()