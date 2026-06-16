# 🤖 Customer Service Chatbot

A Machine Learning and Natural Language Processing (NLP) based Customer Service Chatbot developed using Python, Streamlit, TF-IDF Vectorization, and Logistic Regression.

The chatbot is designed to answer common customer queries related to order tracking, refunds, payments, password resets, technical support, complaints, and customer support services.

---

## 🚀 Features

* NLP-Based Intent Classification
* TF-IDF Vectorization
* Logistic Regression Model
* Confidence-Based Response Handling
* Unknown Query Logging
* Interactive Streamlit Chat Interface
* Chat History Support
* Dark Mode Toggle
* Clear Chat Functionality
* User-Friendly Interface

---

## 🛠 Technologies Used

* Python
* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* TF-IDF Vectorization
* Logistic Regression
* JSON
* Pickle

---

## 📂 Project Structure

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
├── notebooks/
│   └── chatbot_training.ipynb
│
├── screenshots/
│
└── tests/
    ├── test_cases.txt
    └── test_report.md
```

---

## 📥 Clone Repository

```bash
git clone https://github.com/dusssi/Customer-Service-Chatbot.git

cd Customer-Service-Chatbot
```

---

## 🔧 Create Virtual Environment

### Windows PowerShell

```powershell
python -m venv venv

(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned)

.\venv\Scripts\Activate.ps1
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

## 🧠 Train the Model

If the model files are not available, run:

```bash
python train_model.py
```

This generates:

```text
models/
├── chatbot_model.pkl
└── vectorizer.pkl
```

---

## ▶️ Test Chatbot Backend

Run:

```bash
python chatbot.py
```

Example Output:

```text
Please provide your order ID.
```

---

## 🌐 Run the Streamlit Application

Start the chatbot interface:

```bash
streamlit run app.py
```

Open in your browser:

```text
http://localhost:8501
```

---

## 💬 Sample Queries

```text
hello

hi

where is my order

track my package

refund request

payment failed

forgot password

contact support

customer care number

website not working
```

---

## 🧪 Testing

The chatbot was tested using multiple queries covering:

* Greetings
* Order Tracking
* Refund Requests
* Payment Issues
* Password Reset
* Technical Support
* Complaints
* Contact Support
* Unknown Queries

Testing files are available inside:

```text
tests/
├── test_cases.txt
└── test_report.md
```

---

## 📊 Machine Learning Workflow

```text
User Query
      ↓
TF-IDF Vectorization
      ↓
Logistic Regression Model
      ↓
Intent Prediction
      ↓
Response Selection
      ↓
Chatbot Reply
```

---

## 🔮 Future Improvements

* Spell Checking Support
* Expanded Intent Dataset
* Multi-Language Support
* Streamlit Cloud Deployment
* Database Integration
* Real Customer Support API Integration
* User Authentication

---

## 👨‍💻 Developer

**Dushyant Chauhan**

Developed as part of the Artificial Intelligence Internship Program at Codec Technologies.

Built using Python, Machine Learning, NLP, and Streamlit.

GitHub Repository:

https://github.com/dusssi/Customer-Service-Chatbot

---

## ⭐ Acknowledgement

This project was developed for learning and educational purposes to gain practical experience in Machine Learning, Natural Language Processing, Streamlit, and GitHub project development.
