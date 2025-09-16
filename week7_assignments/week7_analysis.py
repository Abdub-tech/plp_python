# week7_analysis.py
# Week 7 Assignment: Analyzing Data with Pandas & Visualizing with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# ------------------------------
# Task 1: Load and Explore Dataset
# ------------------------------
iris = load_iris(as_frame=True)
df = iris.frame  # Convert to pandas DataFrame

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------
print("\nStatistical Summary:")
print(df.describe())

# Grouping: average petal length per species
grouped = df.groupby("target")["petal length (cm)"].mean()
print("\nAverage Petal Length per Species:")
print(grouped)

# ------------------------------
# Task 3: Data Visualizations
# ------------------------------

# Line chart (sepal length trend for first 30 samples)
plt.plot(df["sepal length (cm)"][:30], marker='o')
plt.title("Sepal Length Trend (First 30 Samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# Bar chart (average petal length per species)
grouped.plot(kind="bar", color=["skyblue", "salmon", "lightgreen"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# Histogram (distribution of sepal width)
df["sepal width (cm)"].plot(kind="hist", bins=20, color="purple", alpha=0.7)
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.show()

# Scatter plot (sepal length vs petal length)
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=df["target"], cmap="viridis")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()

# ------------------------------
# Observations
# ------------------------------
# - Different species have clear differences in petal length.
# - Sepal width distribution shows most flowers fall between 2.5–3.5 cm.
# - The scatter plot shows good separation between species groups.

