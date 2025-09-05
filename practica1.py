from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
X = digits.data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=digits.target, cmap="tab10")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA on Digits Dataset")
plt.show()