import pandas as pd
df=pd.read_csv("sales_data_sample.csv",encoding = 'Latin-1')
## if we don't add "",encoding = 'Latin-1'"" then we get error 
df.head()
## so only two columns are important of the dataset i.e. QuantityOrdered and PriceEach other are irrelevant
data=df[['QUANTITYORDERED','PRICEEACH']]
data.head(4)
## Do normalization of the data
from sklearn.preprocessing import StandardScaler
# make object of it
scaler=StandardScaler()
normalized_data=scaler.fit_transform(data)
print(normalized_data)

## Using elbow method , determine the best value of k
# wcss= within cluster sum of squares . It's a measure of how close data points are to the centroid of their cluster

from sklearn.cluster import KMeans

wcss=[]
for i in range(1,16):
    k_means=KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=10)
    # Here
    # n_clusters specifies the number of clusters you want the algorithm to find in your data.
    # init determines the method for initializing the positions of the cluster centers (centroids). 'k-means++'is the default and recommended method.
    # max_iter=300 Sets the maximum number of iterations the algorithm will run for a single initialization.
    # n_init=10 Specifies the number of times the KMeans algorithm will run with different centroid seeds.
    k_means.fit(normalized_data)
    wcss.append(k_means.inertia_)

    ## Elbow Graph
import matplotlib.pyplot as plt
plt.plot(range(1,16),wcss)
plt.xlabel("K value")
plt.ylabel("WCSS")
plt.title("Elbow Curve Graph")

# from graph we can see that for k=4 is the optimal value , so train the model
k_means=KMeans(n_clusters=4,init='k-means++',max_iter=300,n_init=10,random_state=10)
clusters=k_means.fit_predict(normalized_data)
# The fit_predict method combines the operations of fitting the model and predicting

## Visualization of the clusters
plt.scatter(normalized_data[:, 0], normalized_data[:, 1], c=clusters, cmap='viridis')
# x aixs numbers =normalized_data[:, 0]
# y aixs numbers =normalized_data[:, 1]
# The c parameter specifies the color of the markers (data points) in the scatter plot
# The cmap parameter stands for "colormap." It defines the colormap used to map numerical data to colors.
plt.xlabel('QUANTITYORDERED')
plt.ylabel('PRICEEACH')
plt.title('K-Means Clustering')
plt.show()