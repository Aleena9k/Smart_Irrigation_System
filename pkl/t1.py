import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the dataset
df = pd.read_csv("test.csv")

# Encode target variable

# df['Status'] = df['Status'].map({'OFF': 0, 'ON': 1})  # remove this
X = df.drop('Motor', axis=1)
y = df['Motor']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the KNN model with k=3
model_knn3 = KNeighborsClassifier(n_neighbors=3)
model_knn3.fit(X_train, y_train)

# Save the scaler
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Save the trained KNN model
with open('model.pkl', 'wb') as f:
    pickle.dump(model_knn3, f)

print("Scaler and model saved as 'scaler.pkl' and 'model.pkl'.")
