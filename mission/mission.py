
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("mission_launches.csv")


# Display the first few rows of the DataFrame
print(df.head())
# Display information about the DataFrame, including data types and missing values
print(df.info())


# Handle missing values in the 'Price' column
df.dropna(subset=['Price'], inplace=True)

# Data Visualizations

# Mission Status by Organisation
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Organisation', hue='Mission_Status')
plt.title('Mission Status by Organisation')
plt.xlabel('Organisation')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Mission Status')
plt.show()

# Cost Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Price', bins=20, kde=True)
plt.title('Distribution of Mission Costs')
plt.xlabel('Cost (millions)')
plt.ylabel('Frequency')
plt.show()

# Geographical Analysis
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='Location', y='Mission_Status', hue='Organisation')
plt.title('Geographical Distribution of Mission Launches')
plt.xlabel('Location')
plt.ylabel('Mission Status')
plt.xticks(rotation=45)
plt.legend(title='Organisation')
plt.show()

# Mission Details Analysis
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Detail', order=df['Detail'].value_counts().head(10).index)
plt.title('Top 10 Mission Details')
plt.xlabel('Mission Detail')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Temporal Trends
df['Year'] = df['Date'].str.split(', ').str[-1].str[:4]
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Year', order=df['Year'].value_counts().index)
plt.title('Number of Launches by Year')
plt.xlabel('Year')
plt.ylabel('Number of Launches')
plt.xticks(rotation=45)
plt.show()

# Mission Durations
df['Mission_Status_Date'] = pd.to_datetime(df['Mission_Status_Date'])
df['Mission_Duration'] = df['Mission_Status_Date'] - df['Date']
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Mission_Duration', bins=20, kde=True)
plt.title('Distribution of Mission Durations')
plt.xlabel('Mission Duration')
plt.ylabel('Frequency')
plt.show()

#  Success Rate Over Time
success_rate = df.groupby('Year')['Mission_Status'].apply(lambda x: (x == 'Success').sum() / len(x))
plt.figure(figsize=(12, 8))
sns.lineplot(x=success_rate.index, y=success_rate.values)
plt.title('Success Rate of Missions Over Time')
plt.xlabel('Year')
plt.ylabel('Success Rate')
plt.xticks(rotation=45)
plt.show()

#  Cost-effectiveness Analysis
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Mission_Status', y='Price')
plt.title('Cost-effectiveness of Missions')
plt.xlabel('Mission Status')
plt.ylabel('Cost (millions)')
plt.show()
