import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

import reseau

# equally sized bins in log10-scale
bins_log10 = np.logspace(np.log10(reseau.jointProbabilities.min()), np.log10(reseau.jointProbabilities.max()),10)
counts, bin_edges, ignored = plt.hist(reseau.jointProbabilities, bins_log10, histtype = 'bar')

plt.xscale( 'log' )
plt.xlim( bin_edges.min(), bin_edges.max() )
plt.suptitle("Histogramme des probabilitees jointes (ajuste sur un espace log)")
plt.xlabel("Probabilitee jointe")
plt.ylabel("Frequence")

plt.show()