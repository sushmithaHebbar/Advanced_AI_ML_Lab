import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
# --- 1. Load Iris Dataset ---
print("1. Loading Iris dataset...") 
iris = load_iris()
# 4 features
X = iris.data  
# true labels (for reference only)
y_true = iris.target  
N_CLUSTERS = 3
# --- 2. Apply Algorithms ---
print("   Data ready with shape:", X.shape)
# K-Means
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)
kmeans_inertia = kmeans.inertia_
# EM (GMM)
gmm = GaussianMixture(n_components=N_CLUSTERS, random_state=42)
gmm.fit(X)
gmm_labels = gmm.predict(X)
gmm_bic = gmm.bic(X)
# --- 3. Visualization (only first 2 features for clarity) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# K-Means Plot
axes[0].scatter(X[:, 0], X[:, 1], c=kmeans_labels, s=50, cmap='viridis', alpha=0.7) 
axes[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                marker='X', s=200, color='red', label='Centroids')
axes[0].set_title(f'K-Means Clustering (Inertia: {kmeans_inertia:.2f})')
axes[0].set_xlabel(iris.feature_names[0])
axes[0].set_ylabel(iris.feature_names[1])
axes[0].legend()
axes[1].scatter(X[:, 0], X[:, 1], c=gmm_labels, s=50, cmap='viridis', alpha=0.7)# EM (GMM) Plot
axes[1].scatter(gmm.means_[:, 0], gmm.means_[:, 1],
                marker='D', s=200, color='red', label='Means')
axes[1].set_title(f'EM/GMM Clustering (BIC: {gmm_bic:.2f})')
axes[1].set_xlabel(iris.feature_names[0])
axes[1].set_ylabel(iris.feature_names[1])
axes[1].legend()

plt.show()
 # --- 4. Compare Quality ---
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
    print("Inference: The Iris data clusters may be fairly spherical and well-separated.")
elif gmm_score > kmeans_score:
    print("\nObservation: EM/GMM performed better (higher Silhouette Score).")
    print("Inference: The Iris data likely has overlapping or non-spherical clusters.")
else:
    print("\nObservation: Both algorithms achieved very similar scores.")
    print("Inference: The dataset is simple enough for both methods to work equally well.")
