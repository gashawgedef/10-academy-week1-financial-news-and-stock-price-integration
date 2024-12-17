import pandas as pd

def load_data(filepath):
    """
    Load dataset from a CSV file and return a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        print("Data successfully loaded.")
        print(f"Dataset contains {len(df)} rows and {len(df.columns)} columns.")
        print("Columns:", df.columns.tolist())
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}. Please check the path.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


def calculate_headline_length(df):
    """
    Adds a column 'headline_length' to the DataFrame based on the length of the 'headline' column.
    Returns the modified DataFrame.
    """
    if "headline" in df.columns:
        # Fill missing headlines to avoid errors and calculate length
        df["headline"] = df["headline"].fillna("")
        df["headline_length"] = df["headline"].apply(len)
        print("Headline lengths calculated successfully.")
        return df
    else:
        raise KeyError("'headline' column not found in DataFrame")

def articles_per_publisher(df):
    """
    Count and return the number of articles per publisher.
    """
    if "publisher" in df.columns:
        publisher_counts = df["publisher"].value_counts()
        print("Articles per publisher calculated successfully.")
        return publisher_counts
    else:
        raise KeyError("'publisher' column not found in DataFrame")


def analyze_publication_dates(df):
    """
    Analyze and return trends in publication dates.
    The 'date' column is converted to datetime, and article counts are grouped by date.
    """
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        if df["date"].isnull().any():
            print(
                "Warning: Some rows contain invalid date formats and were set to NaT."
            )
        date_counts = df["date"].dt.date.value_counts().sort_index()
        print("Publication date analysis completed successfully.")
        return date_counts
    else:
        raise KeyError("'date' column not found in DataFrame")


def display_eda_summary(df):
    """
    Display a summary of the DataFrame, including column info, null counts, and a preview of the first few rows.
    """
    print("Dataset Information:")
    print(df.info())
    print("\nFirst 5 Rows of Dataset:")
    print(df.head())
    print("\nMissing Values per Column:")
    print(df.isnull().sum())
