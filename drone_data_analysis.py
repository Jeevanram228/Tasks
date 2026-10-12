import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")

#inspecting
print("\n--- First five rows ---")
print(df.head())

print("\n--- Number of rows and columns ---")
print(df.shape)

print("\n--- Column names ---")
print(df.columns.tolist())

print("\n--- Data types and non-null counts ---")
df.info()

print("\n--- Numerical summary ---")
print(df.describe())


#check missing values
print("\n--- Missing values ---")
print(df.isnull().sum())

#check duplicate rows
print("\n--- Duplicate rows ---")
print(df.duplicated().sum())

#inspect unusual values
print("\n--- Negative payload weights ---")
print(df[df["Actual Carry Weight (kg)"] < 0])

print("\n--- Extremely high altitudes ---")
print(df[df["Altitude (meters)"] > 500])

print("\n--- Payload exceeding capacity ---")
print(
    df[df["Actual Carry Weight (kg)"]
       > df["Max Carry Weight (kg)"]]
)

clean = df.copy()

#empty rows and duplicates
clean = clean.dropna(how="all")
clean = clean.drop_duplicates()

print("Original shape:", df.shape)
print("Cleaned shape:", clean.shape)
print("Remaining duplicates:", clean.duplicated().sum())

# Invalid negative payload weights
weight_col = "Actual Carry Weight (kg)"
clean.loc[clean[weight_col] < 0, weight_col] = np.nan

# Missing notes
clean["Notes"] = clean["Notes"].fillna("Not recorded")

#dateformat
clean["Flight Date"] = pd.to_datetime(
    clean["Flight Date"],
    format="%d-%m-%Y",
    errors="coerce"
)

#suspious altitude
print(clean.loc[
    clean["Altitude (meters)"] > 500,
    ["Drone ID", "Altitude (meters)", "Notes"]
])

clean.loc[
    clean["Altitude (meters)"] > 500,
    "Altitude (meters)"
] = np.nan

clean = clean.sort_values("Flight Date")


clean.to_csv("cleaned_drone_data.csv", index=False)

print("Final shape:", clean.shape)
print("Remaining duplicates:", clean.duplicated().sum())
print("Missing values after cleaning:")
print(clean.isnull().sum())


clean.to_csv("cleaned_drone_data.csv", index=False)




#Basic data analysis
print("\n--- Numerical Statistics ---")
print(clean.describe())

print("\n--- Flight Status Counts ---")
print(clean["Flight Status"].value_counts())

print("\n--- Application Counts ---")
print(clean["Application"].value_counts())

print("\n--- Average Flight Duration by Application ---")
print(
    clean.groupby("Application")["Flight Duration (minutes)"]
    .mean()
    .round(2)
)

print("\n--- Average Distance by Application ---")
print(
    clean.groupby("Application")["Distance Flown (km)"]
    .mean()
    .round(2)
)




import matplotlib.pyplot as plt
import seaborn as sns

#Histogram
sns.histplot(
    data=clean,
    x="Altitude (meters)",
    bins=20
)

plt.title("Distribution of Drone Flight Altitudes")
plt.xlabel("Altitude (meters)")
plt.ylabel("Number of flights")
plt.tight_layout()

plt.tight_layout()
plt.savefig("plots/plot1.png", dpi=300, bbox_inches="tight")

plt.show()

#Scatterplot
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=clean,
    x="Distance Flown (km)",
    y="Flight Duration (minutes)"
)

plt.title("Flight Distance vs Flight Duration")
plt.xlabel("Distance Flown (km)")
plt.ylabel("Flight Duration (minutes)")
plt.tight_layout()
plt.savefig("plots/plot2.png", dpi=300, bbox_inches="tight")
plt.show()


#Box plot
plt.figure(figsize=(12, 6))

sns.boxplot(
    data=clean,
    x="Application",
    y="Flight Duration (minutes)"
)

plt.title("Flight Duration by Drone Application")
plt.xlabel("Application")
plt.ylabel("Flight Duration (minutes)")
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig("plots/plot3.png", dpi=300, bbox_inches="tight")
plt.show()

#Battery histogram
plt.figure(figsize=(8, 5))

sns.histplot(
    data=clean,
    x="Battery Remaining (%)",
    bins=20
)

plt.title("Distribution of Remaining Drone Battery")
plt.xlabel("Battery Remaining (%)")
plt.ylabel("Number of flights")

plt.tight_layout()
plt.savefig("plots/plot4.png", dpi=300, bbox_inches="tight")
plt.show()