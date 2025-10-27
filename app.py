import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.analyzer import analyze_feedback, analyze_dataframe

# --------------------------
# Streamlit Page Configuration
# --------------------------
st.set_page_config(page_title="Customer Feedback Analyzer", layout="wide")
st.title("🧠 Customer Feedback Analyzer")
st.write("Analyze customer feedback sentiment instantly — no API required!")

# --------------------------
# Input Selection
# --------------------------
option = st.radio("Choose Input Type:", ["Single Feedback", "Upload CSV"])

# --------------------------
# Single Feedback Analysis
# --------------------------
if option == "Single Feedback":
    user_input = st.text_area("Enter customer feedback:")
    if st.button("Analyze"):
        if user_input.strip():
            result = analyze_feedback(user_input)
            st.success(f"Sentiment: {result['sentiment']}")
            st.write(f"Sentiment Score: `{result['score']}`")
        else:
            st.warning("Please enter some feedback text.")

# --------------------------
# CSV Feedback Analysis
# --------------------------
else:
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of your data:")
        st.dataframe(df.head())

        text_col = st.selectbox("Select the column containing feedback:", df.columns)

        if st.button("Analyze CSV"):
            results_df = analyze_dataframe(df, text_col)
            st.write("### 🧾 Analysis Results")
            st.dataframe(results_df)

            # --------------------------
            # Smaller, Clean Sentiment Distribution
            # --------------------------
            st.write("### 📊 Sentiment Distribution")
            fig, ax = plt.subplots(figsize=(6, 3))
            counts = results_df["sentiment"].value_counts()

            # Colors for sentiments
            color_map = {
                "Positive 😀": "#2ecc71",
                "Negative 😞": "#e74c3c",
                "Neutral 😐": "#f1c40f",
                "No Feedback": "#95a5a6"
            }
            colors = [color_map.get(x, "#3498db") for x in counts.index]

            counts.plot(kind='bar', color=colors, ax=ax, width=0.5)
            ax.set_ylabel("Number of Feedbacks", fontsize=10)
            ax.set_xlabel("Sentiment", fontsize=10)
            ax.set_title("Feedback Sentiment Count", fontsize=12)
            ax.tick_params(axis='x', rotation=0)
            ax.grid(axis='y', linestyle='--', alpha=0.7)

            st.pyplot(fig)
