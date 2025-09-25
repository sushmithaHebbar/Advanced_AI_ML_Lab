import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

# --- Configuration ---
N_CLUSTERS = 3  # The number of clusters to look for
FILE_NAME = 'sample_data.csv'

# --- 1. Dataset Generation and Saving (Replace with your actual CSV loading) ---
print(f"1. Generating a synthetic dataset with {N_CLUSTERS} clusters...")
X, y_true = make_blobs(n_samples=300, centers=N_CLUSTERS, cluster_std=0.8, random_state=42)
df_data = pd.DataFrame(X, columns=['Feature1', 'Feature2'])
df_data.to_csv(FILE_NAME, index=False)
print(f"   Dataset saved to '{FILE_NAME}'.")

# --- 2. Load Data from CSV ---
try:
    df = pd.read_csv(FILE_NAME)
    X = df.values
    print("2. Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found. Please ensure it exists.")
    exit()

# --- 3. Apply K-Means Algorithm ---
print(f"3. Applying K-Means algorithm with k={N_CLUSTERS}...")
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)
kmeans_inertia = kmeans.inertia_
print(f"   K-Means completed. Inertia: {kmeans_inertia:.2f}")

# --- 4. Apply EM Algorithm (Gaussian Mixture Model) ---
print(f"4. Applying EM (GMM) algorithm with components={N_CLUSTERS}...")
gmm = GaussianMixture(n_components=N_CLUSTERS, random_state=42)
gmm.fit(X)
gmm_labels = gmm.predict(X)
gmm_bic = gmm.bic(X)
print(f"   EM (GMM) completed. BIC: {gmm_bic:.2f}")

# --- 5. Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# K-Means Plot
axes[0].scatter(X[:, 0], X[:, 1], c=kmeans_labels, s=50, cmap='viridis', alpha=0.7)
axes[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                marker='X', s=200, color='red', label='Centroids')
axes[0].set_title(f'K-Means Clustering (k={N_CLUSTERS})', fontsize=14)
axes[0].set_xlabel('Feature 1')
axes[0].set_ylabel('Feature 2')
axes[0].legend()

# EM (GMM) Plot
axes[1].scatter(X[:, 0], X[:, 1], c=gmm_labels, s=50, cmap='viridis', alpha=0.7)
axes[1].scatter(gmm.means_[:, 0], gmm.means_[:, 1],
                marker='D', s=200, color='red', label='Means')
axes[1].set_title(f'EM (GMM) Clustering (n_components={N_CLUSTERS})', fontsize=14)
axes[1].set_xlabel('Feature 1')
axes[1].set_ylabel('Feature 2')
axes[1].legend()

plt.tight_layout()
plt.show()
# 

# --- 6. Compare Clustering Quality (using Silhouette Score) ---
print("\n6. Comparing Clustering Quality (Silhouette Score)...")

# Calculate Silhouette Score for K-Means
try:
    kmeans_score = silhouette_score(X, kmeans_labels)
except ValueError:
    kmeans_score = 'N/A (Too few samples for score calculation)'

# Calculate Silhouette Score for EM (GMM)
try:
    gmm_score = silhouette_score(X, gmm_labels)
except ValueError:
    gmm_score = 'N/A (Too few samples for score calculation)'

# Display Results
comparison_df = pd.DataFrame({
    'Algorithm': ['K-Means', 'EM (GMM)'],
    'Silhouette Score': [kmeans_score, gmm_score],
    'Metric (Lower is Better)': [f"Inertia: {kmeans_inertia:.2f}", f"BIC: {gmm_bic:.2f}"]
})

print("\n--- Comparison Table ---")
print(comparison_df.to_markdown(index=False))
print("------------------------")

# --- 7. Comment on Clustering Quality ---
print("\n7. Commentary on Clustering Quality:")
if isinstance(kmeans_score, float) and isinstance(gmm_score, float):
    if kmeans_score > gmm_score:
        print(f"   K-Means had a **higher Silhouette Score** ({kmeans_score:.3f}) than EM ({gmm_score:.3f}).")
        print("   This suggests that, for this dataset, the simple, hard-assignment clusters found by K-Means are more distinct and well-separated than the soft-assignment clusters found by GMM.")
    elif gmm_score > kmeans_score:
        print(f"   EM (GMM) had a **higher Silhouette Score** ({gmm_score:.3f}) than K-Means ({kmeans_score:.3f}).")
        print("   This often happens with datasets where clusters are non-spherical, have varying sizes/densities, or significantly overlap, which GMM's probabilistic model can handle better.")
    else:
        print(f"   Both algorithms achieved a similar Silhouette Score ({kmeans_score:.3f}).")
        print("   This suggests the dataset's clusters are generally well-defined and spherical, which both algorithms handle effectively.")

print("\nGeneral Observations:")
print("K-Means: Assumes clusters are spherical, equally sized, and works by minimizing within-cluster variance. It provides hard assignments  (each point belongs strictly to one cluster).")
print("EM (GMM): Models clusters as a mixture of Gaussian distributions, allowing for non-spherical shapes, varying sizes, and densities. It provides soft assignments (a probability of belonging to each cluster).")

