import numpy as np
import matplotlib.pyplot as plt
import h5py
from scipy.signal import find_peaks

# Load data
config_file = "simulation_config.json"

mem_pot_file = './output/v_report.h5'
weight_file = './output/syn_report.h5'


# load 
f = h5py.File(mem_pot_file,'r')
mem_potential = f['report']['exc_stim']['data']
plt.plot(mem_potential[:,0])

f = h5py.File(weight_file,'r')
weights = f['report']['exc_stim']['data']
plt.plot(weights[:,0])

#df = pd.DataFrame.from_csv("PN_C.csv")

low = mem_potential[4800, 0]
high = max(mem_potential[4800:, 0])
print(high-low)

plt.show()

