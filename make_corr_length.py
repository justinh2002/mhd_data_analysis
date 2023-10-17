import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# latex
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{bm}'
# basics
rcParams['lines.linewidth'] = 1.2
rcParams['font.family'] = 'Arial'
rcParams['font.size'] = 18
rcParams['axes.linewidth'] = 0.8
# x-ticks
rcParams['xtick.top'] = True
rcParams['xtick.direction'] = 'in'
rcParams['xtick.minor.visible'] = True
rcParams['xtick.major.size'] = 6
rcParams['xtick.minor.size'] = 3
rcParams['xtick.major.width'] = 1.5
rcParams['xtick.minor.width'] = 1.5
rcParams['xtick.major.pad'] = 5
rcParams['xtick.minor.pad'] = 5
# y-ticks
rcParams['ytick.right'] = True
rcParams['ytick.direction'] = 'in'
rcParams['ytick.minor.visible'] = True
rcParams['ytick.major.size'] = 6
rcParams['ytick.minor.size'] = 3
rcParams['ytick.major.width'] = 1.5
rcParams['ytick.minor.width'] = 1.5
rcParams['ytick.major.pad'] = 5
rcParams['ytick.minor.pad'] = 5
# legend
rcParams['legend.fontsize'] = 20 #rcParams['font.size']
rcParams['legend.labelspacing'] = 0.2
rcParams['legend.loc'] = 'upper left'
rcParams['legend.frameon'] = False
# figure
rcParams['figure.figsize'] = (8.0, 5.0)
rcParams['figure.dpi'] = 150
rcParams['savefig.dpi'] = 200
rcParams['savefig.bbox'] = 'tight'

time = np.loadtxt(r'times.txt')
corr_length = np.loadtxt(r'corr_length.txt')
x = np.linspace(1e-2,1,100)
eps =  0.5e-1*x**(3.09/17)

plt.loglog(x,eps,ls = '--')

plt.loglog(time[:len(corr_length)],corr_length)
plt.xlabel(r'$t$')
plt.ylabel(r'$\xi_M$')
plt.savefig('corrlength.pdf')