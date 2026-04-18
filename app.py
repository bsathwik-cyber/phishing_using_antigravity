from flask import Flask, render_template, request
import pickle
from features import extract_features

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        url = request.form["url"]

        # Extract features
        features = extract_features(url)

        # Predict
        result = model.predict([features])[0]

        # Output
        if int(result) == -1:
            prediction = "⚠️ Phishing Website"
        else:
            prediction = "✅ Safe Website"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
print("Model expects:", model.n_features_in_)