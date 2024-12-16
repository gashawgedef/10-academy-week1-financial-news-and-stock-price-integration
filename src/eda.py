import pandas as pd

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)

def calculate_headline_length(df):
    """Add a column for headline length and calculate basic statistics."""
    df['headline_length'] = df['headline'].str.len()
    return df['headline_length'].describe()

def articles_per_publisher(df):
    """Count the number of articles per publisher."""
    return df['publisher'].value_counts()

def analyze_publication_dates(df):
    """Analyze trends in publication dates."""
    df['date'] = pd.to_datetime(df['date'])
    return df['date'].dt.date.value_counts().sort_index()
