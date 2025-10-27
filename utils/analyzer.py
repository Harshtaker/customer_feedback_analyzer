import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_feedback(text):
    if pd.isna(text) or str(text).strip() == "":
        return {"feedback": "", "sentiment": "No Feedback", "score": 0}

    text = str(text).strip()
    score = sia.polarity_scores(text)['compound']

    if score >= 0.05:
        sentiment = "Positive 😀"
    elif score <= -0.05:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return {"feedback": text, "sentiment": sentiment, "score": round(score, 2)}

def analyze_dataframe(df, column_name="feedback"):
    results = []
    for feedback in df[column_name]:
        results.append(analyze_feedback(feedback))
    return pd.DataFrame(results)
