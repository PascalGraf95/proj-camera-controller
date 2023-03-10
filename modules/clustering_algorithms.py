from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
import numpy as np


class KMeansClustering:
    def __init__(self, num_clusters):
        self.num_clusters = num_clusters
        if num_clusters == 'auto':
            pass
        else:
            self.kmeans = KMeans(n_clusters=num_clusters, n_init='auto')

    def fit_to_data(self, data, min_clusters=3):
        if self.num_clusters == 'auto':
            scores = []
            for k in range(min_clusters, 10):
                kmeans = KMeans(n_clusters=k, n_init='auto')
                kmeans.fit(data)
                labels = kmeans.labels_
                scores.append(silhouette_score(data, labels, metric='euclidean'))

            optimal_cluster_num = list(range(min_clusters, 10))[np.argmax(scores)]
            print("Optimal Cluster Number is: {}".format(optimal_cluster_num))
            self.kmeans = KMeans(n_clusters=optimal_cluster_num, n_init='auto')
        self.kmeans.fit(data)
        return self.kmeans.labels_

    def predict(self, data):
        return self.kmeans.predict(data)


class DBSCANClustering:
    def __init__(self, eps=0.5):
        self.dbscan = DBSCAN(eps=eps)

    def fit_to_data(self, data):
        self.dbscan.fit(data)
        return self.dbscan.labels_
