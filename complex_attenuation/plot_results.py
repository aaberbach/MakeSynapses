import numpy as np
import matplotlib.pyplot as plt
import h5py
from bmtk.analyzer.cell_vars import _get_cell_report, plot_report
import matplotlib.pyplot as plt
import pandas as pd 
from scipy.signal import find_peaks
import pickle

f = "syn_att.pkl"
file = open(f, 'rb')
res = pickle.load(file)
file.close()
#import pdb; pdb.set_trace()
dists = [key for key in res.keys() ]#if key >= 0.005]
dists = np.sort(dists)
atts = [res[key][0] for key in dists]

plt.figure()
plt.title("Distance from soma vs Attenuation")
plt.xlabel("Distance from soma (um)")
plt.ylabel("Attenuation")
plt.scatter(dists, atts, marker='.', label='w=0.1')
plt.show()

# plt.figure()
# plt.scatter(strengths, uEPSPs, marker='.')
# plt.title("Exc Synapse Conductance vs uEPSPs")
# plt.xticks(strengths)
# plt.xlabel("Exc Synapse Condunctance")
# plt.ylabel("uEPSP (mv)")

# import seaborn as sb
# print(np.mean(uEPSPs), np.std(uEPSPs))
# plt.figure()
# sb.distplot(uEPSPs)
# plt.xscale('log')
# plt.show()