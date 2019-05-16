from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


Data = {'x': [],
        'y': []
       }
for i in grid.houses:
    Data('x').append(thegrid.houses[i].posx)
    Data('Y').append(thegrid.houses[i].posy)

df = DataFrame(Data,columns=['x','y'])

kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
