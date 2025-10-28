# 🧠 Customer Feedback Analyzer

An intelligent **Customer Feedback Analyzer** built using **Python**, **NLTK**, **Deep Translator**, and **Streamlit**.  
It helps analyze customer feedback (in multiple languages) and generates meaningful insights such as **sentiment analysis**, **keyword extraction**, and **data visualization**.

---

## 🚀 Features

- 🌐 **Multilingual Support:** Automatically detects and translates non-English feedback using `deep_translator`.
- 📊 **Sentiment Analysis:** Uses NLTK-based sentiment scoring to classify feedback as **Positive**, **Negative**, or **Neutral**.
- 📈 **Visual Dashboard:** Interactive Streamlit app that displays sentiment distribution, keyword frequencies, and sample feedbacks.
- 📁 **CSV Upload:** Upload your own feedback dataset in `.csv` format.
- 💬 **Text Analyzer:** Instantly analyze any single feedback text from the Streamlit interface.

---

## 🧩 Project Structure

customer_feedback_analyzer/
│
├── app.py # Main Streamlit app
├── requirements.txt # All dependencies
│
├── data/
│ └── sample_feedback.csv # Example multilingual feedback dataset
│
├── utils/
│ ├── analyzer.py # NLP functions and translation logic
│ └── visualizer.py # Data visualization utilities
│
└── README.md # Project documentation


---

## ⚙️ Installation and Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Harshtaker/customer_feedback_analyzer.git
cd customer_feedback_analyzer

2️⃣ Create a virtual environment
python -m venv .venv

3️⃣ Activate the environment

On Windows:

.venv\Scripts\activate


On Mac/Linux:

source .venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt


If any package is missing later (like deep_translator or nltk):

pip install deep_translator nltk streamlit pandas matplotlib

🧠 Run the Application

After setup, run:

streamlit run app.py


Then open the link shown in the terminal (usually http://localhost:8501
).

📊 Example Usage

Upload data/sample_feedback.csv or your own dataset.

The app:

Detects feedback language

Translates to English if needed

Analyzes sentiment (positive / negative / neutral)

Displays visual summaries

🧠 Technologies Used
Category	Tools/Packages
Frontend	Streamlit
NLP	NLTK, Deep Translator
Data	Pandas, Matplotlib
Language	Python 3.12+
🧾 Sample Dataset Format
Feedback ID	Feedback Text
1	The product quality is amazing!
2	No me gustó el servicio.
3	Livraison très rapide, merci !
🧪 Future Enhancements

✅ Integrate automatic language detection

✅ Add aspect-based sentiment analysis

✅ Include word clouds and topic modeling

✅ Deploy using Streamlit Cloud or Render

👨‍💻 Author

Harsh Shukla
📧 harshshukla0303@gmail.com
