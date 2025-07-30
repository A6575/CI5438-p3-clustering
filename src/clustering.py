import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mode
from sklearn.decomposition import PCA

class Kmeans_cluster:
	def __init__(self, n_clusters=3, max_iter=300):
		self.n_clusters = n_clusters
		self.max_iter = max_iter
		self.y_pred = np.array([])
		self.centroids = pd.DataFrame()

	def random_init(self, data):
		centroids = []
		for _ in range(self.n_clusters):
			centroid = data.apply(lambda x: float(x.sample().iloc[0]))
			centroids.append(centroid)
		
		return pd.concat(centroids, axis=1)
	
	def get_labels(self, data):
		distances = self.centroids.apply(lambda x: ((data - x) ** 2).sum(axis=1))
		return distances.idxmin(axis=1)
	
	def new_centroids(self, data, labels):
		centroids = data.groupby(labels).mean().T
		return centroids

	def plot_clusters(self, data, labels, centroids, iteration, func, savefig_name=None):
		pca = PCA(n_components=2)
		data_2d = pca.fit_transform(data)
		centroids_2d = pca.transform(centroids.T)
		func(wait=True)
		plt.title(f'Iteracion {iteration} de K-means Clustering (k={self.n_clusters})')
		plt.scatter(x=data_2d[:,0], y=data_2d[:,1], c=labels)
		plt.scatter(x=centroids_2d[:,0], y=centroids_2d[:,1])
		plt.show()

		if savefig_name is not None:
			plt.savefig(f'../img/parte_2-1/{savefig_name}')
			plt.close()

	def kmeans_algorithm(self, data, func, animation=False, savefig_name=None):
		self.centroids = self.random_init(data)
		old_centroids = pd.DataFrame()

		for i in range(self.max_iter):
			if (self.centroids.equals(old_centroids)):
				break
			
			labels = self.get_labels(data)
			old_centroids = self.centroids
			self.centroids = self.new_centroids(data, labels)
			if animation:
				self.plot_clusters(data, labels, self.centroids, i, func)

		# Guardar la última gráfica si se solicita
		if savefig_name is not None:
			self.plot_clusters(data, labels, self.centroids, i, func, savefig_name)
		
		# Almacenar las predicciones finales como atributo
		self.y_pred = np.array(self.get_labels(data))
	
	def cluster_accuracy(self, y_true):
		labels = np.unique(self.y_pred)
		correct = 0
		for label in labels:
			mask = self.y_pred == label
			if np.any(mask):
				most_common = mode(y_true[mask], keepdims=True)[0][0]
				correct += np.sum(y_true[mask] == most_common)
		return correct / len(y_true)
	
	def plot_collage(self, data, labels, centroids, n_runs, collage_name):
		_, axes = plt.subplots(1, n_runs, figsize=(5*n_runs, 5))
		if n_runs == 1:
			axes = [axes]
		pca = PCA(n_components=2)
		data_2d = pca.fit_transform(data)
		for idx, ax in enumerate(axes): # type: ignore
			centroids_2d = pca.transform(centroids[idx].T)
			ax.set_title(f'Run {idx+1}')
			ax.scatter(x=data_2d[:,0], y=data_2d[:,1], c=labels[idx])
			ax.scatter(x=centroids_2d[:,0], y=centroids_2d[:,1], marker='X', s=100, c='red')
		plt.tight_layout()
		plt.suptitle(f'Collage de los Resultados de K-means Clustering para k={self.n_clusters}', fontsize=16, y=1.05)
		if collage_name is not None:
			plt.savefig(f'../img/parte_2-1/{collage_name}')
		plt.show()
		plt.close()

	def multiple_runs(self, data, y_true, func, n_runs=5, animation=False, collage_name=None):
		results = []
		accuracies = []
		final_labels = []
		final_centroids = []
		for i in range(n_runs):
			print("*"*10, f"Run {i+1}/{n_runs}", "*"*10)
			self.kmeans_algorithm(data, func, animation)
			labels = self.get_labels(data)
			final_labels.append(labels)
			final_centroids.append(self.centroids.copy())

			# Calcula la suma de distancias cuadradas (inercia)
			inertia = ((data - self.centroids.T.loc[labels].values) ** 2).sum().sum()
			results.append(inertia)
			accuracies.append(self.cluster_accuracy(y_true))
			print(f">>> Inertia = {inertia:.6f} | Accuracy = {self.cluster_accuracy(y_true):.6f}")

		print("\n" + "*"*30)
		print(f">>> Average inertia: {np.mean(results):.6f}")
		print(f">>> Best (min) inertia: {np.min(results):.6f}")
		print(f">>> Worst (max) inertia: {np.max(results):.6f}")
		print(f">>> Average accuracy: {np.mean(accuracies):.6f}")

		# Crear collage de gráficos finales
		self.plot_collage(data, final_labels, final_centroids, n_runs, collage_name)
		return results
