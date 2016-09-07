import numpy as np 
import scipy.spatial.distance as spadis
import matplotlib as mpl 
import matplotlib.cm as cm

def contact(A):
	## initialize data matrices
	## A is expected to be a N x 3 position matrices
	[m, n] = A.shape

	## distance matrix, where DIST[i,j] is the distance between sample i and j
	DIST = np.zeros([m, n])
	x = range(0, m)
	y = range(m, 0, -1)

	## compute the pairwise distance among each row of A
	## Returns a condensed distance matrix Y. For each i and j (where i<j<n), the metric dist(u=X[i], v=X[j]) is computed and stored in entry ij.
	## shape of dis is (m * (m - 1) / 2, 1)
	dis = spadis.pdist(A, 'euclidean')

	## fill the distance matrix from dis
	idx = 0
	for i in range(m):
		for j in range(i + 1, m):
			DIST[i, j] = dis[idx]
			DIST[j, i] = DIST[i, j]
			idx += 1

	## plot the grayscale colormap
	fig = plt.figure()
	plt.pcolormesh(x, y, DIST, cmap = cm.gray)
	plt.colorbar()

	plt.title('Contact Map Test')
	plt.savefig('contact_map.png')
	plt.show()

	return fig

A = np.load('block2000.npy')
fig = contact(A)