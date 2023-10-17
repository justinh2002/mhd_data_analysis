from matplotlib import rcParams
import numpy as np
import matplotlib.pyplot as plt

rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{bm}'
# basics
rcParams['lines.linewidth'] = 1.2
rcParams['font.family'] = 'Arial'
rcParams['font.size'] = 17
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
rcParams['legend.fontsize'] = 15 #rcParams['font.size']
rcParams['legend.labelspacing'] = 0.2
rcParams['legend.loc'] = 'upper left'
rcParams['legend.frameon'] = False
# figure
rcParams['figure.figsize'] = (8.0, 5.0)
rcParams['figure.dpi'] = 150
rcParams['savefig.dpi'] = 200
rcParams['savefig.bbox'] = 'tight'


x_velhelicity = np.loadtxt(r'velhelicity_flux_x.txt')
y_velhelicity = np.loadtxt(r'vel_helicity_cor.txt')

x_adotv = np.loadtxt(r'adotv_flux_x.txt')
y_adotv = np.loadtxt(r'adotv_flux.txt')

x_gaugehel = np.loadtxt(r'gaugehelicity_flux_x.txt')
y_gaugehel = np.loadtxt(r'gaugehelicity_flux.txt')

plt.loglog(x_velhelicity[y_velhelicity  >0 ],y_velhelicity[y_velhelicity > 0],label ='Positive, vel. helicity', color = 'blue',marker = 'o')
plt.loglog(x_velhelicity[y_velhelicity <0 ],np.abs(y_velhelicity[y_velhelicity<0]),label ='Negative, vel. helicity', color = 'red',marker = 'o')

plt.loglog(x_adotv[y_adotv  >0 ],y_adotv[y_adotv > 0],label ='Positive, adotv', color = 'black',marker = 'x')
plt.loglog(x_adotv[y_adotv <0 ],np.abs(y_adotv[y_adotv<0]),label ='Negative, adotv', color = 'green',marker = 'x')

plt.loglog(x_gaugehel[y_gaugehel  >0 ],y_gaugehel[y_gaugehel > 0],label ='Positive, gauge', color = 'purple',marker = '^')
plt.loglog(x_gaugehel[y_gaugehel <0 ],np.abs(y_gaugehel[y_gaugehel<0]),label ='Negative, gauge', color = 'orange',marker = '^')


plt.legend()
plt.xlabel('r')
plt.ylabel('correlators')
plt.savefig('test.pdf',dpi = 300)