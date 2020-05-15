#%%
import os
import pickle
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

# Configure Matplotlib style parameters
plt.rcParams.update(mpl.rcParamsDefault)
mpl_params = {
        'font.family' : 'Arial',
        'font.size' : 8, # Science 6-10pt, Nature 5-9pt, APL minimum 8pt
        'mathtext.fontset' : 'dejavuserif',
        'ytick.labelsize': 9,
        'ytick.labelsize': 9,
        'xtick.major.size': 3.5,
        'ytick.major.size': 3.5,
        'xtick.minor.size': 2.0,
        'ytick.minor.size': 2.0,
        'lines.linewidth': 0.5,
        'axes.linewidth' : 0.5,
        'xtick.major.width' : 0.5,
        'ytick.major.width' : 0.5,
        'xtick.minor.width' : 0.5,
        'ytick.minor.width' : 0.5,
        }
plt.rcParams.update(mpl_params)
plt.ion()
colors = ['#a6611a', '#dfc27d', '#80cdc1', '#018571']
          
# Configure figure parameters
figure_filename = 'count_ratio_snspd_sweep'
width = 4
ratio = 1.618
height = width/ratio
fig, ax = plt.subplots()
fig.set_size_inches(width, height)
ax.set_xlabel('SNSPD current (μA)')
ax.set_ylabel('Ratio')
ax.set_xlim([26, 32])
ax.set_ylim([-.1, 1.1])
ax.set_title('Ratio of SNSPD count rate to readout count ratio\nvs. SNSPD bias current')

# Import data
data_filepath = r'C:/Users/jgamm/Desktop/superconductivity_paper/data'
l, u = .5, 1.
with open(os.path.join(data_filepath, 'D1_ratio_sweeping_snspd_current_ireadout8u.pickle'), 'rb') as F:
    Dev1 = pickle.load(F)
    Dev1['ratio'] = [0 if Dev1['snspd count rate'][i]==0 \
         else Dev1['readout count rate'][i]/Dev1['snspd count rate'][i] \
         for i in range(len(Dev1['readout count rate']))]
    [a, b] = (np.array(Dev1['ratio'])!=0).nonzero()[0].take((0, -1))
    Dev1['average ratio'] = np.mean(Dev1['ratio'] \
        [np.int(np.floor(a+l*(b-a))) : np.int(np.ceil(a+u*(b-a)))])
with open(os.path.join(data_filepath, 'D2_ratio_sweeping_snspd_current_ireadout7.5u.pickle'), 'rb') as F:
    Dev2 = pickle.load(F)
    Dev2['ratio'] = [0 if Dev2['snspd count rate'][i]==0 \
         else Dev2['readout count rate'][i]/Dev2['snspd count rate'][i] \
         for i in range(len(Dev2['readout count rate']))]
    [a, b] = (np.array(Dev2['ratio'])!=0).nonzero()[0].take((0, -1))
    Dev2['average ratio'] = np.mean(Dev2['ratio'] \
        [np.int(np.floor(a+l*(b-a))) : np.int(np.ceil(a+u*(b-a)))])
with open(os.path.join(data_filepath, 'D3_ratio_sweeping_snspd_current_ireadout18u.pickle'), 'rb') as F:
    Dev3 = pickle.load(F)
    Dev3['ratio'] = [0 if Dev3['snspd count rate'][i]==0 \
         else Dev3['readout count rate'][i]/Dev3['snspd count rate'][i] \
         for i in range(len(Dev3['readout count rate']))]
    [a, b] = (np.array(Dev3['ratio'])!=0).nonzero()[0].take((0, -1))
    Dev3['average ratio'] = np.mean(Dev3['ratio'] \
        [np.int(np.floor(a+l*(b-a))) : np.int(np.ceil(a+u*(b-a)))])
with open(os.path.join(data_filepath, 'D4_ratio_sweeping_snspd_current_ireadout19u.pickle'), 'rb') as F:
    Dev4 = pickle.load(F)
    Dev4['ratio'] = [0 if Dev4['snspd count rate'][i]==0 \
         else Dev4['readout count rate'][i]/Dev4['snspd count rate'][i] \
         for i in range(len(Dev4['readout count rate']))]
    [a, b] = (np.array(Dev4['ratio'])!=0).nonzero()[0].take((0, -1))
    Dev4['average ratio'] = np.mean(Dev4['ratio'] \
        [np.int(np.floor(a+l*(b-a))) : np.int(np.ceil(a+u*(b-a)))])

# Create plot
data_style_args = dict(
    marker = 'o',
    #markersize = 7,
    fillstyle='none',
    linestyle='None')
avg_style_args = dict(
    linestyle = '--',
    linewidth = 1.0)

ax.plot(Dev1['readout bias'], Dev1['ratio'],
        color = colors[0],
        label = 'Device 1',
        markersize=7.5,
        zorder = 4,
        **data_style_args)
ax.plot(Dev2['readout bias'], Dev2['ratio'],
        color = colors[1],
        label = 'Device 2',
        markersize=6,
        zorder = 5,
        **data_style_args)
ax.plot(Dev3['readout bias'], Dev3['ratio'],
        color = colors[2],
        label = 'Device 3',
        markersize=4.5,
        zorder = 6,
        **data_style_args)
ax.plot(Dev4['readout bias'], Dev4['ratio'],
        color = colors[3],
        label = 'Device 4',
        markersize=3,
        zorder = 7,
        **data_style_args)
ax.plot(Dev4['readout bias'], [Dev1['average ratio'] for i in Dev4['readout bias']],
        color = colors[0],
        label =  'Mean = %.03f'%(Dev1['average ratio']),
        zorder = 0,
        **avg_style_args)
ax.plot(Dev4['readout bias'], [Dev2['average ratio'] for i in Dev4['readout bias']],
        color = colors[1],
        label = 'Mean = %.03f'%(Dev2['average ratio']),
        zorder = 1,
        **avg_style_args)
ax.plot(Dev4['readout bias'], [Dev3['average ratio'] for i in Dev4['readout bias']],
        color = colors[2],
        label = 'Mean = %.03f'%(Dev3['average ratio']),
        zorder = 2,
        **avg_style_args)
ax.plot(Dev4['readout bias'], [Dev4['average ratio'] for i in Dev4['readout bias']],
        color = colors[3],
        label = 'Mean = %.03f'%(Dev4['average ratio']),
        zorder = 3,
        **avg_style_args)
ax.legend(ncol=2, loc='lower right').set_zorder(8)
plt.tight_layout()

# Save data
output_filepath = r'C:/Users/jgamm/Desktop/superconductivity_paper/figures'
fig.savefig(os.path.join(output_filepath, figure_filename+'.pdf'), dpi=300)
