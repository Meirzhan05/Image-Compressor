import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

file_name = input("Enter the name of the file containing the data: ")



original_img = plt.imread(f"data/{file_name}")
print("Shape of original_img is:", original_img.shape)
X_img = np.reshape(original_img, (original_img.shape[0] * original_img.shape[1], 3))

if file_name.endswith("jpg") or file_name.endswith("jpeg"):
    X_img = X_img / 255
print("Shape of X_img is:", X_img.shape)

kmeans = KMeans(n_clusters=100, random_state=0)

kmeans.fit(X_img)

labels = kmeans.predict(X_img)

# Get the list of closest centroids to every training example
compressed_img = kmeans.cluster_centers_[kmeans.labels_]
compressed_img = np.reshape(compressed_img, (original_img.shape[0], original_img.shape[1], 3))

# Calculate the memory used by the original image (in bytes)
original_memory = original_img.size * original_img.itemsize
print(f"Original memory: {original_memory} bytes")

# Calculate the memory used by the compressed image (in bytes)
# Each color is represented by 3 bytes (for RGB), and there's one color per cluster
compressed_memory = kmeans.n_clusters * 3
print(f"Compressed memory: {compressed_memory} bytes")

# Calculate the memory saved
memory_saved = original_memory - compressed_memory
print(f"Memory saved: {memory_saved} bytes")

# Calculate the percentage of memory saved
percentage_saved = (memory_saved / original_memory) * 100
print(f"Percentage of memory saved: {percentage_saved}%")

fig, ax = plt.subplots(1, 2, figsize=(12, 8))
plt.axis('off')

ax[0].imshow(original_img)
ax[0].set_title('Original Image')
ax[0].set_axis_off()
ax[1].imshow(compressed_img)
ax[1].set_title('Compressed Image')
ax[1].set_axis_off()
plt.show()



