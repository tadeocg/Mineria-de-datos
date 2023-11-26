import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load CSV file
file = 'playlist limpio.csv'
data = pd.read_csv(file)

# Select columns for clustering
columns_for_clustering = ['track_popularity', 'number_of_tracks_in_album']
data_for_clustering = data[columns_for_clustering]

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_clustering)

# Apply K-Means
n_clusters = 3  # Adjust the number of clusters as needed
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_data)

# Print the cluster assignments
print("Cluster Assignments:")
print(data['Cluster'])

# Save results to a new CSV file
output_file = 'file.csv'
data.to_csv(output_file, index=False)
