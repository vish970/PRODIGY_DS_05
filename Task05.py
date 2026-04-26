# Task05.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/Users/Vishal.S/OneDrive/Pictures/Screenshots/prodigy internship/prodigy_DS_01/US_Accidents_March23.csv", nrows=100000)  # first 100k rows

print("Dataset shape:", data.shape)
print(data.head())

plt.figure(figsize=(10,6))
sns.countplot(y="Weather_Condition", data=data, order=data["Weather_Condition"].value_counts().iloc[:10].index)
plt.title("Top 10 Weather Conditions During Accidents")
plt.savefig("outputs/weather_conditions.png")
plt.close()

# -----------------------------
# Accident Distribution by Road Condition
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="Crossing", data=data)  
plt.title("Accidents by Road Features")
plt.savefig("outputs/road_conditions.png")
plt.close()

# -----------------------------
# Accident Distribution by Time of Day
# -----------------------------
data["Start_Time"] = pd.to_datetime(data["Start_Time"])
data["Hour"] = data["Start_Time"].dt.hour

plt.figure(figsize=(10,6))
sns.countplot(x="Hour", data=data, palette="coolwarm")
plt.title("Accidents by Hour of Day")
plt.savefig("outputs/time_of_day.png")
plt.close()

print("Outputs saved in outputs/ folder.")
