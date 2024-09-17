Sentiment Analysis and Visualization of Twitter Data

Overview :

This task is part of my Data Science internship at Prodigy InfoTech. I worked on analyzing and visualizing sentiment data from two datasets (training and validation) containing tweets and posts related to various brands/topics. The goal was to clean the data, merge the datasets, and then visualize the distribution of sentiment categories, as well as the breakdown of sentiment across the top 10 brands/topics.

Objective :

The main objective of this task was to:
Load, inspect, and clean two datasets (training and validation).
Merge the datasets for a unified analysis.
Analyze the distribution of sentiment labels (e.g., Positive, Negative, Neutral, Irrelevant).
Visualize sentiment distribution and breakdown by brand/topic to gain insights into how different brands are perceived.

Key Features of the Code :

Data Loading:
Loaded two datasets (training and validation) using Pandas.

Data Cleaning:
Removed missing values using dropna().
Renamed columns for consistency between the two datasets (such as ID, Brand, Sentiment, and Text).

Data Merging:
Combined the cleaned datasets using pd.concat() for unified analysis.

Sentiment Analysis:
Analyzed the distribution of sentiment categories using value_counts().

Visualization:
Created a bar chart of the sentiment distribution using Seaborn’s countplot() with labeled data points.
Generated a second bar chart to break down sentiment categories by the top 10 brands/topics, also using Seaborn’s countplot().

Learning Outcomes :
Data Cleaning: Developed skills in identifying and handling missing data, renaming columns for consistency, and merging datasets.

Sentiment Analysis: Gained insights into sentiment distribution across a large dataset, using basic aggregation methods (value_counts()).

Data Visualization: Improved proficiency in visualizing categorical data using Seaborn and Matplotlib, including adding data labels and customizing plots.

Brand Sentiment: Learned to break down and visualize sentiment data by specific categories (top 10 brands/topics).
Tools & Technologies

Python (Version 3.x): Core language for data handling and visualization.
Pandas: For data loading, cleaning, and combining datasets.
Seaborn: For creating the sentiment distribution and brand/topic breakdown plots.
Matplotlib: For plot customization and display.

Sample Output :
The visualizations generated provided a clear breakdown of the sentiment distribution and the relationship between sentiment and brands/topics. The labeled bar charts offered insights into how different brands are perceived in terms of positive, negative, neutral, or irrelevant sentiment categories.
