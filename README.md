# 🤖 Customer Service Chatbot

A simple NLP-based Customer Service Chatbot built using Python, Streamlit, TF-IDF Vectorization, and Logistic Regression.

The chatbot can answer customer queries related to:

* Order Tracking
* Refund Requests
* Payment Issues
* Password Reset
* Technical Support
* Product Information
* Customer Complaints
* Contact Support

---

## Features

* NLP-based Intent Classification
* TF-IDF Vectorization
* Logistic Regression Model
* Confidence Threshold Handling
* Unknown Query Logging
* Interactive Streamlit Chat Interface
* Dark Mode Toggle
* Chat History Support

---

## Technologies Used

* Python
* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* TF-IDF
* Logistic Regression
* JSON

---

## Project Structure

```text
Customer-Service-Chatbot/
│
├── app.py
├── chatbot.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── intents.json
│
├── models/
│   ├── chatbot_model.pkl
│   └── vectorizer.pkl
│
├── logs/
│   └── unmatched_queries.txt
│
├── screenshots/
│
└── tests/
```

## Installation

```bash
git clone <repository-url>

cd Customer-Service-Chatbot

pip install -r requirements.txt

streamlit run app.py
```

## Sample Questions

```text
hello

where is my order

track my package

refund request

forgot password

payment failed
```

## Future Improvements

* Add Spell Checking
* Expand Intent Dataset
* Deploy on Streamlit Cloud
* Add Database Support
* Integrate with Real Customer Support APIs

## Developer

**Dushyant**

Built using Python, Machine Learning, and Streamlit.
