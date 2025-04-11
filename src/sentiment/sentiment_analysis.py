from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # -1 to 1
    sentiment = "Positive" if sentiment_score > 0.2 else "Negative" if sentiment_score < -0.2 else "Neutral"
    
    return {
        "Sentiment": sentiment,
        "Polarity": round(sentiment_score, 3),
        "Subjectivity": round(blob.sentiment.subjectivity, 3)
    }
