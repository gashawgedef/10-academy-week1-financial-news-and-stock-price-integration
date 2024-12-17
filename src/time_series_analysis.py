import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset and ensure the 'date' column is in datetime format


import pandas as pd


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
    publication_count = df.groupby(df["date"].dt.to_period("M")).size()
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
