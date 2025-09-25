import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import os

# --- Configuration ---
N_CLUSTERS = 3
FILE_NAME = 'sample_data.csv'

# --- 1. Generate & Load Data ---
print("1. Generating and loading data...")
X, _ = make_blobs(n_samples=300, centers=N_CLUSTERS, cluster_std=0.8, random_state=42)
pd.DataFrame(X, columns=['Feature1', 'Feature2']).to_csv(FILE_NAME, index=False)
df = pd.read_csv(FILE_NAME)
X = df.values
print("   Data ready.")

# --- 2. Apply Algorithms ---
# K-Means
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)
kmeans_inertia = kmeans.inertia_

# EM (GMM)
gmm = GaussianMixture(n_components=N_CLUSTERS, random_state=42)
gmm.fit(X)
gmm_labels = gmm.predict(X)
gmm_bic = gmm.bic(X)

# --- 3. Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# K-Means Plot
axes[0].scatter(X[:, 0], X[:, 1], c=kmeans_labels, s=50, cmap='viridis', alpha=0.7)
axes[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, color='red', label='Centroids')
axes[0].set_title(f'K-Means (Inertia: {kmeans_inertia:.2f})')

# EM (GMM) Plot
axes[1].scatter(X[:, 0], X[:, 1], c=gmm_labels, s=50, cmap='viridis', alpha=0.7)
axes[1].scatter(gmm.means_[:, 0], gmm.means_[:, 1], marker='D', s=200, color='red', label='Means')
axes[1].set_title(f'EM/GMM (BIC: {gmm_bic:.2f})')

plt.show()

# --- 4. Compare Quality & Comment ---
kmeans_score = silhouette_score(X, kmeans_labels)
gmm_score = silhouette_score(X, gmm_labels)

comparison_df = pd.DataFrame({
    'Algorithm': ['K-Means', 'EM (GMM)'],
    'Silhouette Score': [f"{kmeans_score:.4f}", f"{gmm_score:.4f}"],
    'Internal Metric': [f"Inertia: {kmeans_inertia:.2f}", f"BIC: {gmm_bic:.2f}"]
})

print("\n--- Clustering Comparison ---")
print(comparison_df.to_markdown(index=False))

print("\n--- Commentary on Clustering Quality ---")
print(f"K-Means Silhouette: {kmeans_score:.4f} | EM/GMM Silhouette: {gmm_score:.4f}")

if kmeans_score > gmm_score:
    print("\nObservation: K-Means performed better (higher Silhouette Score).")
    print("Inference: The synthetic data's clusters are likely **spherical, equally-sized, and well-separated**, matching K-Means' core assumptions and leading to clearer hard assignments.")
elif gmm_score > kmeans_score:
    print("\nObservation: EM/GMM performed better (higher Silhouette Score).")
    print("Inference: The data likely has **non-spherical clusters or varying densities**, which GMM's probabilistic model (soft assignments) handles more effectively.")
else:
    print("\nObservation: Both algorithms achieved very similar scores.")
    print("Inference: The data's structure is simple enough for both hard (K-Means) and soft (GMM) assignments to yield similar, high-quality results.")

# Clean up the generated file
os.remove(FILE_NAME)
print(f"\nClean up: Removed '{FILE_NAME}'.")

