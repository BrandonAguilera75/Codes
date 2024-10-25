import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

varianza_explicada_acumulada = np.cumsum(pca.explained_variance_ratio_)

num_componentes_80 = np.argmax(varianza_explicada_acumulada >= 0.80) + 1


plt.figure(figsize=(10, 6))
plt.plot(varianza_explicada_acumulada, marker='o')
plt.axhline(y=0.80, color='r', linestyle='--')
plt.axvline(x=num_componentes_80 - 1, color='r', linestyle='--')
plt.xlabel('Número de componentes')
plt.ylabel('Varianza explicada acumulada')
plt.title('Varianza explicada acumulada por PCA')
plt.show()
componentes_principales = X_pca[:, :2]

plt.figure(figsize=(10, 6))
plt.scatter(componentes_principales[:, 0], componentes_principales[:, 1], c=y, cmap='viridis')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Gráfica de las 2 características más relevantes (PCA)')
plt.colorbar(label='Progreso de la enfermedad')
plt.show()