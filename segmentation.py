import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage import data
from skimage.segmentation import random_walker
from skimage.transform import resize

# load sample image
image = data.camera()
image = resize(image, (150, 150), anti_aliasing=True)

pixels = image.reshape((-1, 1))

# k means to make fg and bg more distinct
kmeans = KMeans(n_clusters=2, random_state=42, n_init="auto")
cluster_labels = kmeans.fit_predict(pixels)

clustered_image = kmeans.cluster_centers_[cluster_labels].reshape(image.shape)

# manual seed
markers = np.zeros(image.shape, dtype=np.uint)

# bg seed. point at sky
markers[10:40, 100:140] = 1 

# fg seed. on person
markers[100:110, 15:40] = 2 

segmented_labels = random_walker(clustered_image, markers, beta=130, mode='bf')

# visualization
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(image, cmap='gray')
axes[0].set_title('1. Original Camera Image')

axes[1].imshow(clustered_image, cmap='gray')
axes[1].set_title('2. K-Means (k=3)')


axes[2].imshow(clustered_image, cmap='gray')
axes[2].imshow(markers, cmap='magma', alpha=0.5)
axes[2].set_title('3. Manual Seeds (Yellow=Man, Pink=Sky)')

axes[3].imshow(segmented_labels, cmap='gray')
axes[3].set_title('4. Final Segmentation')

for ax in axes:
    ax.axis('off')
    
plt.tight_layout()
plt.show()