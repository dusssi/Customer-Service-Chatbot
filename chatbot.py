import json
import random
import pickle


with open("data/intents.json", "r") as file:
    intents = json.load(file)

with open("models/chatbot_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


def predict_intent(message):

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)

    confidence = max(probability[0])

    return prediction, confidence


def get_response(intent):

    for item in intents["intents"]:

        if item["tag"] == intent:

            return random.choice(
                item["responses"]
            )


def chatbot_response(message):

    intent, confidence = predict_intent(
        message
    )

    if confidence < 0.20:
        with open(
            "logs/unmatched_queries.txt",
            "a"
        ) as file:
            file.write(
                message + "\n"
            )

        return (
            "Sorry, I couldn't "
            "understand your request."
        )

    return get_response(intent)


