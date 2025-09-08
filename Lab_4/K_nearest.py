import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
target_names = iris.target_names

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train kNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Function for dynamic test classification
def classify_dynamic_test():
    print("\nChoose a test sample index (0 to", len(X_test) - 1, ")")
    idx = int(input("Enter test sample index: "))

    if idx < 0 or idx >= len(X_test):
        print("Invalid index!")
        return

    # Get sample
    X_sample = X_test[idx].reshape(1, -1)
    y_true = y_test[idx]
    y_pred = knn.predict(X_sample)[0]

    # Print result
    print(f"\nTest Sample {idx}:")
    print(f"   True Label      : {target_names[y_true]}")
    print(f"   Predicted Label : {target_names[y_pred]}")

    if y_pred == y_true:
        print(" Prediction is CORRECT!")
    else:
        print(" Prediction is FALSE!")

    # Plot result
    plt.figure(figsize=(6, 5))
    plt.scatter(X_test[:, 0], X_test[:, 2], c="lightgray", label="Other Test Samples")

    if y_pred == y_true:
        plt.scatter(X_sample[:, 0], X_sample[:, 2], c="green", marker="o", s=120, label="Correct Prediction")
    else:
        plt.scatter(X_sample[:, 0], X_sample[:, 2], c="red", marker="x", s=120, label="False Prediction")

    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Petal length (cm)")
    plt.title("Dynamic kNN Prediction on Iris")
    plt.legend()
    plt.show()

# Run multiple times
while True:
    classify_dynamic_test()
    cont = input("\nDo you want to test another sample? (y/n): ").strip().lower()
    if cont != "y":
        break
