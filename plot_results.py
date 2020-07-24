import numpy as np
import matplotlib.pyplot as plt
import h5py
from bmtk.analyzer.cell_vars import _get_cell_report, plot_report
import matplotlib.pyplot as plt
import pandas as pd 
from scipy.signal import find_peaks
import pickle

#want 0.401 and 0.31
#0.1344 and 0.10257
#strengths = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 25, 30, 50]
#strengths = [0, 2, 4, 6, 8, 10]
# f = "syn_epsps.pkl"
# file = open(f, 'rb')
# res = pickle.load(file)
# file.close()
# #import pdb; pdb.set_trace()
# strengths = [key for key in res.keys() if key >= 0.005]
# strengths = np.sort(strengths)
# uEPSPs = [res[key] for key in strengths]
# print(res)

# plt.figure()
# plt.scatter(strengths, uEPSPs, marker='.')
# plt.title("Exc Synapse Conductance vs uEPSPs")
# plt.xticks(strengths)
# plt.xlabel("Exc Synapse Condunctance")
# plt.ylabel("uEPSP (mv)")
#plt.xscale('log')

f = "dist_test.pkl"
file = open(f, 'rb')
res = pickle.load(file)
file.close()
#import pdb; pdb.set_trace()
strengths = [key for key in res.keys() ]#if key >= 0.005]
strengths = np.sort(strengths)
uEPSPs = [res[key] for key in strengths]

# plt.figure()
# plt.scatter(strengths, uEPSPs, marker='.')
# plt.title("Exc Synapse Conductance vs uEPSPs")
# plt.xticks(strengths)
# plt.xlabel("Exc Synapse Condunctance")
# plt.ylabel("uEPSP (mv)")

import seaborn as sb
print(np.mean(uEPSPs), np.std(uEPSPs))
plt.figure()
sb.distplot(uEPSPs)
plt.xscale('log')
plt.show()