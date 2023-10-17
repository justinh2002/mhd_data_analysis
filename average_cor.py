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


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# written by Christoph Federrath, 2023

import numpy as np
import argparse
import cfpack as cfp
from cfpack import print, hdfio, stop


# Initialize lists to store x and y data for each seed
x_data = {}
y_data = {}

# Loop over seed numbers from seed2 to seed20
for i in range(2, 21):
    # Construct the file name with the current seed number
    fn = f'Turb_hdf5_plt_cnt_0001_sf_adotvflux_seed{i}.dat'
    
    
        # Read the file
    tab = cfp.read_ascii(fn)
    
    # Extract the data from the table and append to the respective lists
    x = tab["#01_GridStag"].data
    y = tab["#04_SF(long,order=01)"].data
    
    x_data[f'seed{i}'] = x
    y_data[f'seed{i}'] = y
        

# Now x_data and y_data lists contain the x and y data from all files respectively
# You can now process these lists further as needed

# Initialize a variable to store the sum of y values for each position
sum_y = None

# Count the number of seed datasets
num_seeds = 0

# Loop over seed numbers from seed2 to seed20

# Initialize variables
sum_y = None
sum_y_squared = None
num_seeds = 0

all_y = []

# Loop over seed numbers from seed2 to seed20
for i in range(2, 21):
    seed_key = f'seed{i}'
    
    # Check if the seed key exists in the y_data dictionary
    if seed_key in y_data:
        # Append the y values for the current seed to the all_y list
        all_y.append(y_data[seed_key])
# Loop over seed numbers from seed2 to seed20
for i in range(2, 21):
    seed_key = f'seed{i}'
    
    # Check if the seed key exists in the y_data dictionary
    if seed_key in y_data:
        # Convert the y values for the current seed to a numpy array
        current_y = np.array(y_data[seed_key])
        
        # If sum_y is None, initialize it; else, add current_y to sum_y
        if sum_y is None:
            sum_y = current_y
            sum_y_squared = current_y ** 2  # initializing sum of squared y values
        else:
            sum_y += current_y
            sum_y_squared += current_y ** 2  # adding squared y values to the sum
        
        # Increment the seed counter
        num_seeds += 1
    else:
        # Print a warning if the seed key is not found in y_data
        print(f"Warning: {seed_key} not found in y_data")

all_y_array = np.array(all_y)
# Calculate and print the average and standard deviation of y values
if num_seeds > 0 and sum_y is not None:  # avoid division by zero
    average_y = sum_y / num_seeds
    # calculate variance (mean of squared differences)
    variance_y = (sum_y_squared / num_seeds) - (average_y ** 2)
    std_dev_y = np.std(all_y_array, axis=0)  
    # calculate standard deviation (square root of variance)
    #std_dev_y = np.sqrt(variance_y)
    print(f"The average of y values across seeds from seed2 to seed20 is: {average_y}")
    print(f"The standard deviation of y values across seeds from seed2 to seed20 is: {std_dev_y}")
else:
    print("No y values found")


x = np.linspace(0.008,0.03,100)
y = 1e-17 * x**(-4)
plt.loglog(x_data['seed2'][average_y  >0 ],x_data['seed2'][average_y  >0 ]**(3)*average_y[average_y > 0],label ='Positive', color = 'blue',marker = 'o')
plt.loglog(x_data['seed2'][average_y <0 ],average_y[average_y<0],label ='Negative', color = 'red',marker = 'o')
plt.errorbar(x_data['seed2'],x_data['seed2']**(3)*average_y,xerr= None, yerr = x_data['seed2']**(3)*std_dev_y,ls = '',capsize=5,marker = '',markersize = 13)
plt.loglog(x,y,label = r'$r^{-4}$')
plt.ylabel(r'$r^3\langle v_i a_j b_k a_\ell b_m \rangle \delta_{jk} \delta_{\ell m }$')
plt.xlabel(r'$r$')
#print(std_dev_y)
plt.legend()

np.savetxt('adotv_flux_x.txt',x_data['seed2'])


#plt.savefig('compensated_helicity.pdf')
#plt.show()

dC_dr = np.gradient(average_y[average_y > 0])
plt.semilogx(x_data['seed2'][average_y  >0 ], dC_dr/average_y[average_y > 0]**(4/3))
plt.ylabel(r'$dC/dr/C^{4/3}$')
plt.xlabel(r'$r$')
plt.ylim(-2500,2500)
#plt.savefig('lim_corr_vel_flux.pdf')
plt.show()