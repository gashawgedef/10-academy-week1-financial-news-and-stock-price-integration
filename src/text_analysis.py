from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def perform_sentiment_analysis(df):
    """Perform sentiment analysis on headlines."""
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df[['headline', 'sentiment']]

def extract_common_keywords(df, n=10):
    """Extract the most common keywords from headlines."""
    vectorizer = CountVectorizer(stop_words='english', max_features=n)
    X = vectorizer.fit_transform(df['headline'])
    keywords = vectorizer.get_feature_names_out()
    return pd.DataFrame({'Keyword': keywords})
