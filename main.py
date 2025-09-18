import pandas as pd

# Load your dataset (replace with your actual file)
df = pd.read_csv('your_dataset.csv')

# View the first 5 rows
print(df.head())

# Check the column names and data types
print(df.info())

# Summary statistics for numeric columns
print(df.describe())
# Check for missing values in each column
print(df.isnull().sum())

# Optional: Check the percentage of missing values
missing_percent = df.isnull().mean() * 100
print(missing_percent)
{
    "cells": [
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {
                "collab": {
                    
                },
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "\n",
                "# Load your dataset (replace with your actual file)\n",
                "df = pd.read_csv('your_dataset.csv')\n",
                "\n",
                "# View the first 5 rows\n",
                "print(df.head())\n",
                "\n",
                "# Check the column names and data types\n",
                "print(df.info())\n",
                "\n",
                "# Summary statistics for numeric columns\n",
                "print(df.describe())\n",
                "# Check for missing values in each column\n",
                "print(df.isnull().sum())\n",
                "\n",
                "# Optional: Check the percentage of missing values\n",
                "missing_percent = df.isnull().mean() * 100\n",
                "print(missing_percent)"
            ]
        }