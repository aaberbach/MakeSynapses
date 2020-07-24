import sys, os
from bmtk.simulator import bionet
import numpy as np
import h5py
import synapses
import pickle




if __name__ == '__main__':
    if __file__ != sys.argv[-1]:
        inp = sys.argv[-1]
    else:
        raise Exception("no work" + str(sys.argv[-1]))

weight = float(inp)

synapses.set_pyr_w(weight)
synapses.load()

config_file = 'simulation_config.json'

conf = bionet.Config.from_json(config_file, validate=True)
conf.build_env()

graph = bionet.BioNetwork.from_config(conf)
sim = bionet.BioSimulator.from_config(conf, network=graph)
sim.run()

cur_file = './output/se_clamp_report.h5'

# load 
f = h5py.File(cur_file,'r')
cur = f['data']
# import matplotlib.pyplot as plt
# plt.plot(cur[:, 0])

# plt.show()

low = cur[5000, 0]
high = max(cur[5000:, 0])
mag = high - low
print(mag * 1000)

f = open('inh_test.pkl', 'rb')
res = pickle.load(f)
res[weight] = mag * 1000
f.close()

f = open('inh_test.pkl', 'wb')
pickle.dump(res, f)
f.close()