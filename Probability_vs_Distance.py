import numpy as np
import matplotlib.pyplot as plt


def ProbabilityCalculation(A, TAD_size, start):
	# A is the contact frequency matrix
	[m, n] = A.shape
	normalizationFactor = A.max(axis=1).max(axis=0)

	# cut the matrix ubti 300-monomer TADs, 600-monomer TADs, and 1200-monomer
	# TADs. 
	end = start + TAD_size
	TADs = A[start : end, start : end]

	probabilities = []

	# Calculate the average probabilities of the line offset from diagonal, and append it 
	for i in range(0, TAD_size):
		diagonalSum = 0
		for j in range(0, TAD_size - i):
			diagonalSum += A[j + i][j] + A[j][j + i]
		digonalMean = diagonalSum / float((TAD_size - i) * 2)
		probabilities.append(digonalMean)

	probabilities = np.asarray(probabilities, dtype = float) / normalizationFactor

	# logarithmically bin the probabilities array for a log-log plot
	bin_edge_index = []
	iterator = 0
	power = 0
	while iterator < TAD_size:
		iterator = 7*1.2**power
		bin_edge_index.append(iterator)
		power+=1
	bin_edge_index = np.asarray(bin_edge, dtype = int)
	bin_edge_index[bin_edge.size - 1] = TAD_size - 1
	# bin_edge = probabilities[bin_edge_index]
	# digitized = numpy.digitize(probabilities, bin_edge)
	# bin_means = [probabilities[digitized == i].mean() for i in range(1, len(bin_edge))]

	# bin array according to bin_edge_index
	bin_probabilities = []
	bin_probabilities.append(mean(probabilities[0:bin_edge_index[0]]))
	for i in range(1, bin_edge_index.size):
		bin_probabilities.append(mean(probabilities[bin_edge_index[i-1] : bin_edge_index[i]]))
	bin_probabilities = np.asarray(bin_probabilities)

	# plot log plot
	x = range(0, bin_probabilities.size)
	x = np.asarray(x)
	fig = plt.figure()
	plt.plot(x, bin_probabilities)
	plt.ylabel('Contact probability P(s)')
	plt.xlabel('monomer distance (0.6kb)')
	plt.title('P(s) vs. monomer distance (logarithmically spaced)')


