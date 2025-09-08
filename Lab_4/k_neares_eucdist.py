import numpy as np
from collections import Counter

# Dataset: size, color, weight
X_train = [
    [100, 0, 50],  # cucumber green
    [150, 2, 80],  # carrot orange
    [120, 1, 60],  # tomato red
    [130, 0, 55],  # cucumber green
    [170, 2, 90],  # carrot orange
    [110, 1, 65],  # tomato red
]

y_train = ['cucumber', 'carrot', 'tomato', 'cucumber', 'carrot', 'tomato']

# Color encoding
color_map = {'green': 0, 'red': 1, 'orange': 2}

def euclidean_distance(a, b):
    return np.sqrt(np.sum((np.array(a) - np.array(b)) ** 2))

def knn_classify(X_train, y_train, X_new, k=3):
   
    distances = []
    for i, x in enumerate(X_train):
        dist = euclidean_distance(x, X_new)
        distances.append((dist, y_train[i]))
    
    #sort the distance nearer to the K size
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    
    # Count the classes of k nearest neighbors
    classes = [label for _, label in k_nearest]
    count = Counter(classes)
    
#most common class
    return count.most_common(1)[0][0]

def classify_dynamic():
    size = float(input("Enter size: "))
    color = input("Enter color (green/red/orange): ").strip().lower()
    weight = float(input("Enter weight: "))
    actual_class = input("Enter actual class (cucumber/carrot/tomato): ").strip().lower()
    
    if color not in color_map:
        print("Unknown color! Please enter green, red, or orange.")
        return
    
    color_encoded = color_map[color]
    X_new = [size, color_encoded, weight]
    
    predicted = knn_classify(X_train, y_train, X_new, k=3)
    print(f"Predicted vegetable: {predicted}")

    if predicted.lower() == actual_class:
        print("Prediction is CORRECT.")
    else:
        print("Prediction is FALSE.")
        
classify_dynamic()
