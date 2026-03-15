import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('../data/plant_signals.csv')

# Select features
X = data[['moisture','temperature','electrical_signal']]
y = data['plant_state']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)

print("Plant Stress Detection Model Accuracy:", accuracy)
