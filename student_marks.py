import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dataset Definition
names = [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "]
marks = ["72", "85", "absent", "64", "90", "78", "81", "69"]

df = pd.DataFrame({'Name': names, 'Marks': marks})

# 2. Data Cleaning
df['Name'] = df['Name'].str.strip().str.title()
df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print("Cleaned Student Marks DataFrame:")
print(df)

# 3. Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Marks'], color='skyblue', edgecolor='black')
plt.title('Student Marks Distribution')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. Save Image
script_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(script_dir, 'marks_bar.png'), dpi=300, bbox_inches='tight')
plt.show()