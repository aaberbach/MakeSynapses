from bmtk.builder import NetworkBuilder
import numpy as np
import sys
import synapses

synapses.load()
syn = synapses.syn_params_dicts()

# if __name__ == '__main__':
#     if __file__ != sys.argv[-1]:
#         inp = sys.argv[-1]
#     else:
#         raise Exception("no work" + str(sys.argv[-1]))

# weight = float(inp)
#find 0.2 mv
net = NetworkBuilder("biophysical")

net.add_nodes(N=1, pop_name='PyrC',
              potental='exc',
              model_type='biophysical',
              model_template='ctdb:Biophys1.hoc',
              model_processing='aibs_perisomatic',
              dynamics_params='472363762_fit.json',
              morphology='Scnn1a_473845048_m.swc')
# net.add_nodes(N=1, pop_name='PyrC',
#         mem_potential='e',
#         model_type='biophysical',
#         model_template='hoc:stylized_typeC',
#         morphology=None)

inh_stim = NetworkBuilder('inh_stim')
inh_stim.add_nodes(N=1,
                pop_name='inh_stim',
                potential='exc',
                model_type='virtual')

# Create connections between Exc --> Pyr cells
net.add_edges(source=inh_stim.nodes(), target=net.nodes(),
                connection_rule=1,
                syn_weight=1,
                delay=0.1,
                dynamics_params='INT2PN.json',
                model_template=syn['INT2PN.json']['level_of_detail'],
                distance_range=[9, 10],
                target_sections=['somatic'])

# Build and save our networks
net.build()
net.save_nodes(output_dir='network')
net.save_edges(output_dir='network')

inh_stim.build()
inh_stim.save_nodes(output_dir='network')

import h5py
f = h5py.File('inh_stim_spikes.h5', 'w')
f.create_group('spikes')
f['spikes'].create_group('inh_stim')
f['spikes']['inh_stim'].create_dataset("node_ids", data=[0])
f['spikes']['inh_stim'].create_dataset("timestamps", data=[500])
f.close()

from bmtk.utils.sim_setup import build_env_bionet

build_env_bionet(base_dir='./',
                network_dir='./network',
                tstop=700.0, dt = 0.1,
                report_vars=['v'],
                clamp_reports=['se'],#Records se clamp currents.
                se_voltage_clamp={
                    "amps":[[-40, -70, -70]],
                    "durations": [[1000, 0, 0]],
                    'gids': [0],
                    'rs': [0.01],
                }, 
                spikes_inputs=[('inh_stim', 'inh_stim_spikes.h5')],
                components_dir='biophys_components',
                include_examples=True,
                compile_mechanisms=True)