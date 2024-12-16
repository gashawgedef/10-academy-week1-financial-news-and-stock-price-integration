import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from src.eda import (
    load_data,
    calculate_headline_length,
    articles_per_publisher,
    analyze_publication_dates,
)
from src.text_analysis import perform_sentiment_analysis, extract_common_keywords
from src.time_series_analysis import publication_frequency_over_time, peak_publishing_times

def main():
    filepath = "data/raw_analyst_ratings.csv"  # Replace with your actual data path
    df = load_data(filepath)
    
    # Descriptive Statistics
    print("Headline Length Statistics:")
    print(calculate_headline_length(df))
    
    print("\nArticles Per Publisher:")
    print(articles_per_publisher(df))
    
    print("\nPublication Trends Over Time:")
    print(analyze_publication_dates(df))
    
    # Text Analysis
    print("\nSentiment Analysis:")
    print(perform_sentiment_analysis(df).head())
    
    print("\nCommon Keywords:")
    print(extract_common_keywords(df))
    
    # Time Series Analysis
    print("\nPublication Frequency Over Time:")
    print(publication_frequency_over_time(df))
    
    print("\nPeak Publishing Times:")
    print(peak_publishing_times(df))

if __name__ == '__main__':
    main()
