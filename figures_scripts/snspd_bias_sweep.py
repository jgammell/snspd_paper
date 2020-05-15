#%%
import os
import pickle
import matplotlib as mpl
from matplotlib import pyplot as plt

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
figure_filename = 'snspd_bias_sweep'
width = 4
ratio = 1.618
height = width/ratio
fig, ax = plt.subplots()
fig.set_size_inches(width, height)
ax.set_xlabel('Bias current (μA)')
ax.set_ylabel('Count rate (Hz)')
ax.set_yscale('symlog')
ax.set_title('SNSPD: count rate vs. bias current')

# Import data
data_filepath = r'C:\Users\jgamm\Documents\GitHub\snspd_paper\data'
with open(os.path.join(data_filepath, 'D1_SNSPD_bias_sweep.pickle'), 'rb') as F:
    Dev1 = pickle.load(F)
with open(os.path.join(data_filepath, 'D2_SNSPD_bias_sweep.pickle'), 'rb') as F:
    Dev2 = pickle.load(F)
with open(os.path.join(data_filepath, 'D3_SNSPD_bias_sweep.pickle'), 'rb') as F:
    Dev3 = pickle.load(F)
with open(os.path.join(data_filepath, 'D4_SNSPD_bias_sweep.pickle'), 'rb') as F:
    Dev4 = pickle.load(F)

# Create plot
mpl_style_args = dict(
    marker = 'o',
    #markersize = 7,
    fillstyle='none',
    linestyle='None')

ax.plot(Dev1['bias values'], Dev1['count rates'],
        color = colors[0],
        label = 'Device 1',
        markersize=7.5,
        **mpl_style_args)
ax.plot(Dev2['bias values'], Dev2['count rates'],
        color = colors[1],
        label = 'Device 2',
        markersize=6,
        **mpl_style_args)
ax.plot(Dev3['bias values'], Dev3['count rates'],
        color = colors[2],
        label = 'Device 3',
        markersize=4.5,
        **mpl_style_args)
ax.plot(Dev4['bias values'], Dev4['count rates'],
        color = colors[3],
        label = 'Device 4',
        markersize=3,
        **mpl_style_args)
ax.legend()
plt.tight_layout()

# Save data
output_filepath = r'C:\Users\jgamm\Documents\GitHub\snspd_paper\figures'
fig.savefig(os.path.join(output_filepath, figure_filename+'.pdf'), dpi=300)
