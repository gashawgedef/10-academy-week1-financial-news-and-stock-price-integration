import pandas as pd

def publication_frequency_over_time(df):
    """Analyze publication frequency over time."""
    df['date'] = pd.to_datetime(df['date'])
    return df['date'].dt.to_period('D').value_counts().sort_index()

def peak_publishing_times(df):
    """Find times when most articles are published."""
    df['time'] = pd.to_datetime(df['date']).dt.time
    return df['time'].value_counts().head(10)
