import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import nltk

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception:
        return text  

def analyze_feedback(text):
    if pd.isna(text) or str(text).strip() == "":
        return {"feedback": "", "sentiment": "No Feedback", "score": 0}

    text = str(text).strip()
    translated_text = translate_to_english(text)
    score = sia.polarity_scores(translated_text)['compound']

    if score >= 0.05:
        sentiment = "Positive 😀"
    elif score <= -0.05:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return {
        "original_text": text,
        "translated_text": translated_text,
        "sentiment": sentiment,
        "score": round(score, 2)
    }

def analyze_dataframe(df, column_name="feedback"):
    results = []
    for feedback in df[column_name]:
        results.append(analyze_feedback(feedback))
    return pd.DataFrame(results)
