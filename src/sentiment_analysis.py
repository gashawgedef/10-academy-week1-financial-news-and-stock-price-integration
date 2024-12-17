# src/sentiment_analysis.py

import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer


def perform_sentiment_analysis(df):
    """
    Perform sentiment analysis on headlines.
    - Sentiment polarity is a float between -1 (negative) and 1 (positive).
    """
    df["sentiment"] = df["headline"].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df[["headline", "sentiment"]]


def extract_common_keywords(df, n=10):
    """
    Extract the most common keywords from headlines.
    - Uses CountVectorizer to extract n most frequent keywords.
    """
    vectorizer = CountVectorizer(stop_words="english", max_features=n)
    X = vectorizer.fit_transform(df["headline"])
    keywords = vectorizer.get_feature_names_out()
    return pd.DataFrame({"Keyword": keywords})


def load_data(filepath):
    """
    Load the dataset from a CSV file.
    """
    df = pd.read_csv(filepath)
    return df
