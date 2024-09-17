import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
training_data = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\PRODIGY_DS_04\twitter_training.csv')
validation_data = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\PRODIGY_DS_04\twitter_validation.csv')

# Data Cleaning: Remove missing values
training_data_cleaned = training_data.dropna()
validation_data_cleaned = validation_data.dropna()

# Renaming columns for consistency
training_data_cleaned.columns = ['ID', 'Brand', 'Sentiment', 'Text']
validation_data_cleaned.columns = ['ID', 'Brand', 'Sentiment', 'Text']

# Combine both datasets for unified analysis
combined_data = pd.concat([training_data_cleaned, validation_data_cleaned], ignore_index=True)

# Analyze the sentiment distribution
sentiment_counts = combined_data['Sentiment'].value_counts()

# Visualize the sentiment distribution with data labels
plt.figure(figsize=(10, 6))
ax = sns.countplot(x='Sentiment', data=combined_data, palette='viridis',
                   order=combined_data['Sentiment'].value_counts().index)

# Add labels
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')

# Add title and labels
plt.title('Sentiment Distribution with Counts', fontsize=16)
plt.xlabel('Sentiment', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=0)

# Show the plot
plt.show()

# Breakdown of sentiments by brand/topic
plt.figure(figsize=(12, 8))
sns.countplot(x='Brand', hue='Sentiment', data=combined_data, palette='viridis', 
              order=combined_data['Brand'].value_counts().index[:10])  # Top 10 brands/topics

# Add title and labels
plt.title('Sentiment Breakdown by Top 10 Brands/Topics', fontsize=16)
plt.xlabel('Brand/Topic', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=90)

# Show the plot
plt.show()
