# descriptive_statistics.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    """
    Load dataset from a CSV file.
    """
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
    return df


def headline_length_statistics(df):
    """
    Calculate and display headline length statistics.
    """
    df["headline_length"] = df["headline"].apply(
        lambda x: len(x.split())
    )  # Word count in headline
    print("\nBasic Statistics for Headline Lengths:")
    print(df["headline_length"].describe())

    # Plot distribution of headline lengths
    plt.figure(figsize=(10, 6))
    sns.histplot(df["headline_length"], bins=20, kde=True, color="skyblue")
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Number of Words in Headline")
    plt.ylabel("Frequency")
    plt.show()


def articles_per_publisher(df):
    """
    Count and display the number of articles per publisher.
    """
    publisher_counts = df["publisher"].value_counts()
    print("\nNumber of Articles Per Publisher:")
    print(publisher_counts)

    # Plot top publishers
    plt.figure(figsize=(12, 6))
    publisher_counts.head(10).plot(kind="bar", color="orange")
    plt.title("Top 10 Publishers by Number of Articles")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.show()

# def publication_date_trends(df):
#     """
#     Analyze trends in publication dates.
#     """
#     # Ensure 'date' column exists and convert it to datetime
#     if "date" not in df.columns:
#         print("Error: 'date' column not found in DataFrame!")
#         return

#     df["date"] = pd.to_datetime(df["date"])  # Use the 'date' column

#     # Count articles per day
#     daily_counts = df.groupby(df["date"].dt.date).size()
#     print("\nPublication Frequency Over Time:")
#     print(daily_counts.head())

#     # Plot publication trends
#     plt.figure(figsize=(12, 6))
#     daily_counts.plot(kind="line", color="purple")
#     plt.title("Trends in Article Publications Over Time")
#     plt.xlabel("Publication Date")
#     plt.ylabel("Number of Articles Published")
#     plt.show()
# def publication_date_trends(df):
#     """
#     Analyze trends in publication dates.
#     """
#     # Check for a column with a date-related name
#     possible_columns = ["publication_date", "date", "publish_date"]
#     date_column = next((col for col in possible_columns if col in df.columns), None)

#     if not date_column:
#         print("Error: No date-related column found in DataFrame!")
#         return

#     # Convert the found column to datetime
#     df["date"] = pd.to_datetime(df[date_column], errors="coerce")

#     # Count articles per day
#     daily_counts = df.groupby(df["date"].dt.date).size()
#     print("\nPublication Frequency Over Time:")
#     print(daily_counts.head())

#     # Plot publication trends
#     plt.figure(figsize=(12, 6))
#     daily_counts.plot(kind="line", color="purple")
#     plt.title("Trends in Article Publications Over Time")
#     plt.xlabel("Publication Date")
#     plt.ylabel("Number of Articles Published")
#     plt.show()


# def articles_by_day_of_week(df):
#     """
#     Analyze frequency of articles by day of the week.
#     """
#     # Ensure date is datetime format
#     if "date" not in df.columns:
#         print("Error: 'date' column not found in DataFrame!")
#         return

#     df["date"] = pd.to_datetime(df["date"])  # Correct column name to 'date'

#     # Extract day of the week
#     df["day_of_week"] = df["date"].dt.day_name()

#     # Count articles per day of the week
#     day_counts = df["day_of_week"].value_counts()
#     print("\nArticles Published by Day of the Week:")
#     print(day_counts)

#     # Plot frequency by day of the week
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x=day_counts.index, y=day_counts.values, palette="coolwarm")
#     plt.title("Articles Published by Day of the Week")
#     plt.xlabel("Day of the Week")
#     plt.ylabel("Number of Articles")
#     plt.show()