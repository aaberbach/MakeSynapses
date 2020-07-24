import numpy as np
import matplotlib.pyplot as plt
import h5py
from bmtk.analyzer.cell_vars import _get_cell_report, plot_report
import matplotlib.pyplot as plt
import pandas as pd 
from scipy.signal import find_peaks
import pickle
import seaborn as sb

def lognormal(m, s):
        mean = np.log(m) - 0.5 * np.log((s/m)**2+1)
        std = np.sqrt(np.log((s/m)**2 + 1))
        return max(np.random.lognormal(mean, std, 1), 0.0000000001)
#1.9, 1.4
m = 1.9
s = 1.4

dist = [float(lognormal(m, s)) for i in range(10000)]

plt.figure()
sb.distplot(dist)

plt.figure()
sb.distplot(dist)
plt.xscale('log')

plt.show()

