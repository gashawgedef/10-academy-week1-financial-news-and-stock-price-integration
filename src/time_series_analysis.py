# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns


# # Load the dataset and ensure the 'date' column is in datetime format


# import pandas as pd


# def load_data(filepath):
#     """
#     Load the dataset and parse the 'date' column into datetime objects with timezone awareness.
#     """
#     df = pd.read_csv(filepath)

#     # Print the first few rows of the date column for inspection
#     print("Sample Date Values Before Parsing:")
#     print(df["date"].head())

#     try:
#         # Parse dates with timezone-aware datetime
#         df["date"] = pd.to_datetime(df["date"], utc=True, errors="coerce")
#     except Exception as e:
#         print(f"Error while parsing dates: {e}")

#     # Display rows with invalid date values
#     print("\nRows with Invalid Date Values:")
#     print(df[df["date"].isna()])

#     # Drop rows where date could not be parsed
#     df = df.dropna(subset=["date"])

#     return df


# # Time Series Analysis: Publication Frequency Over Time
# def publication_frequency_over_time(df):
#     """
#     Analyze the publication frequency over time.
#     """
#     df["date"] = pd.to_datetime(
#         df["date"], errors="coerce"
#     )  # Ensure 'date' column is in datetime format
#     publication_count = df.groupby(df["date"].dt.to_period("M")).size()
#     return publication_count


# # Time Series Analysis: Analyzing Publishing Times
# def analyze_publishing_times(df):
#     """
#     Analyze the publishing times to see if there are specific trends or patterns.
#     """
#     df["hour"] = df["date"].dt.hour  # Extract the hour from the datetime
#     publishing_times = df.groupby("hour").size()
#     return publishing_times


# # Publisher Analysis: Articles Per Publisher
# def articles_per_publisher(df):
#     """
#     Analyze the number of articles per publisher.
#     """
#     publisher_stats = df["publisher"].value_counts()
#     return publisher_stats


# # Publisher Analysis: Extract Unique Publisher Domains
# def extract_unique_publisher_domains(df):
#     """
#     Extract the unique domains from publisher emails or names.
#     """
#     # Extract the domain part from the publisher's email (if applicable)
#     df["publisher_domain"] = df["publisher"].str.extract(
#         r"@([a-zA-Z0-9.-]+)", expand=False
#     )
#     unique_domains = df["publisher_domain"].value_counts()
#     return unique_domains
# time_series_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    """
    Load the dataset and parse the 'date' column into datetime objects with timezone awareness.
    """
    df = pd.read_csv(filepath)

    # Print the first few rows of the date column for inspection
    print("Sample Date Values Before Parsing:")
    print(df["date"].head())

    try:
        # Parse dates with timezone-aware datetime
        df["date"] = pd.to_datetime(df["date"], utc=True, errors="coerce")
    except Exception as e:
        print(f"Error while parsing dates: {e}")

    # Display rows with invalid date values
    print("\nRows with Invalid Date Values:")
    print(df[df["date"].isna()])

    # Drop rows where date could not be parsed
    df = df.dropna(subset=["date"])

    return df


# Time Series Analysis: Publication Frequency Over Time
def publication_frequency_over_time(df):
    """
    Analyze the publication frequency over time.
    """
    df["date"] = pd.to_datetime(
        df["date"], errors="coerce"
    )  # Ensure 'date' column is in datetime format
    publication_count = df.groupby(
        df["date"].dt.to_period("M")
    ).size()  # Count articles by month
    return publication_count


# Time Series Analysis: Analyzing Publishing Times
def analyze_publishing_times(df):
    """
    Analyze the publishing times to see if there are specific trends or patterns.
    """
    df["hour"] = df["date"].dt.hour  # Extract the hour from the datetime
    publishing_times = df.groupby("hour").size()
    return publishing_times


# Publisher Analysis: Articles Per Publisher
def articles_per_publisher(df):
    """
    Analyze the number of articles per publisher.
    """
    publisher_stats = df["publisher"].value_counts()
    return publisher_stats


# Publisher Analysis: Extract Unique Publisher Domains
def extract_unique_publisher_domains(df):
    """
    Extract the unique domains from publisher emails or names.
    """
    # Extract the domain part from the publisher's email (if applicable)
    df["publisher_domain"] = df["publisher"].str.extract(
        r"@([a-zA-Z0-9.-]+)", expand=False
    )
    unique_domains = df["publisher_domain"].value_counts()
    return unique_domains


# Plotting: Publication Frequency Over Time
def plot_publication_frequency(publication_count):
    """
    Plot the publication frequency over time.
    """
    plt.figure(figsize=(12, 6))
    publication_count.plot(kind="line")
    plt.title("Publication Frequency Over Time (Monthly)", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Number of Articles", fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Plotting: Analyzing Publishing Times
def plot_publishing_times(publishing_times):
    """
    Plot the publishing times distribution.
    """
    plt.figure(figsize=(12, 6))
    publishing_times.plot(kind="bar", color="skyblue")
    plt.title("Number of Articles Published by Hour of Day", fontsize=16)
    plt.xlabel("Hour of Day", fontsize=12)
    plt.ylabel("Number of Articles", fontsize=12)
    plt.grid(axis="y")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# Plotting: Articles Per Publisher
def plot_articles_per_publisher(publisher_stats):
    """
    Plot the number of articles per publisher.
    """
    plt.figure(figsize=(12, 6))
    publisher_stats.head(10).plot(kind="bar", color="lightcoral")
    plt.title("Top 10 Publishers by Number of Articles", fontsize=16)
    plt.xlabel("Publisher", fontsize=12)
    plt.ylabel("Number of Articles", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Plotting: Unique Publisher Domains
def plot_unique_publisher_domains(unique_domains):
    """
    Plot the unique publisher domains.
    """
    plt.figure(figsize=(12, 6))
    unique_domains.head(10).plot(kind="bar", color="lightgreen")
    plt.title("Top 10 Publisher Domains", fontsize=16)
    plt.xlabel("Publisher Domain", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
