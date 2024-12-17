import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud

# Download necessary resources from NLTK
nltk.download("punkt")
nltk.download("stopwords")

def extract_common_keywords(df, n=10):
    """
    Extract the most common keywords from headlines.
    - Uses CountVectorizer to extract n most frequent keywords.
    """
    vectorizer = CountVectorizer(stop_words="english", max_features=n)
    X = vectorizer.fit_transform(df["headline"])
    keywords = vectorizer.get_feature_names_out()
    return pd.DataFrame({"Keyword": keywords})
# Sentiment Analysis function
def perform_sentiment_analysis(df):
    """
    Perform sentiment analysis on the headlines to classify them as Positive, Negative, or Neutral.
    """

    def get_sentiment(text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"

    df["sentiment"] = df["headline"].apply(get_sentiment)
    return df


# Preprocess text for LDA (Tokenization, Removing stopwords)
def preprocess_text(text):
    """
    Preprocess text by tokenizing and removing stop words.
    """
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    filtered_words = [
        word for word in words if word.isalpha() and word not in stop_words
    ]
    return filtered_words


# Topic Modeling using LDA
def perform_topic_modeling(df, num_topics=5):
    """
    Perform LDA topic modeling on the headlines to extract topics.
    """
    df["processed_headlines"] = df["headline"].apply(preprocess_text)

    dictionary = corpora.Dictionary(df["processed_headlines"])
    corpus = [dictionary.doc2bow(text) for text in df["processed_headlines"]]

    lda_model = gensim.models.LdaMulticore(
        corpus, num_topics=num_topics, id2word=dictionary, passes=10, workers=2
    )

    topics = lda_model.print_topics(num_words=5)
    for topic in topics:
        print(topic)

    return lda_model, topics


# Function to plot Sentiment Distribution
def plot_sentiment_distribution(df):
    """
    Plot the sentiment distribution (positive, negative, neutral).
    """
    sentiment_counts = df["sentiment"].value_counts()
    plt.figure(figsize=(6, 6))
    sentiment_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        colors=["lightgreen", "salmon", "lightblue"],
    )
    plt.title("Sentiment Distribution")
    plt.ylabel("")  # Remove the y-label for better presentation
    plt.show()


# Function to plot Word Cloud for Topics
def plot_word_cloud(df, lda_model):
    """
    Plot a word cloud for the most frequent words across all headlines.
    """
    all_words = [word for text in df["processed_headlines"] for word in text]
    word_freq = {word: all_words.count(word) for word in set(all_words)}

    # Generate and plot word cloud
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of All Headlines")
    plt.show()


# Function to plot Top Words per Topic
def plot_top_words_per_topic(lda_model, num_topics=5):
    """
    Plot the top words for each topic identified by LDA.
    """
    for t in range(num_topics):
        plt.figure(figsize=(10, 6))
        words = lda_model.show_topic(t, topn=10)
        words = [word for word, _ in words]
        plt.barh(
            range(len(words)),
            [weight for _, weight in lda_model.show_topic(t, topn=10)],
            color="skyblue",
        )
        plt.yticks(range(len(words)), words)
        plt.title(f"Top 10 Words in Topic {t + 1}")
        plt.xlabel("Word Frequency")
        plt.ylabel("Words")
        plt.show()

def extract_common_keywords(df, n=10):
    """
    Extract common keywords from the headlines using CountVectorizer.
    """
    vectorizer = CountVectorizer(stop_words="english", max_features=n)
    X = vectorizer.fit_transform(df["headline"])
    keywords = vectorizer.get_feature_names_out()
    counts = X.sum(axis=0).A1
    keyword_df = pd.DataFrame(
        list(zip(keywords, counts)), columns=["Keyword", "Frequency"]
    )
    keyword_df = keyword_df.sort_values(by="Frequency", ascending=False)
    return keyword_df




# Function to plot common keywords
def plot_common_keywords(keyword_df):
    """
    Plot the top n common keywords and their counts.
    """
    plt.figure(figsize=(10, 6))
    plt.barh(keyword_df["Keyword"], keyword_df["Count"], color="skyblue")
    plt.xlabel("Keyword Frequency")
    plt.ylabel("Keyword")
    plt.title("Top Common Keywords in Headlines")
    plt.gca().invert_yaxis()  # Invert y-axis to display the highest frequency at the top
    plt.show()


# Load data function
def load_data(file_path):
    """
    Load dataset from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df
