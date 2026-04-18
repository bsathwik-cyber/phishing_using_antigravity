import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from features import extract_features

# Load dataset
data = pd.read_csv("dataset.csv")

# Drop index column
if 'index' in data.columns:
    data = data.drop('index', axis=1)

# IMPORTANT: Generate features from URL
if 'url' in data.columns:
    data['features'] = data['url'].apply(extract_features)
    X = pd.DataFrame(data['features'].tolist())
else:
    # fallback (if dataset already numeric)
    X = data.drop("Result", axis=1)

y = data["Result"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained with correct features!")