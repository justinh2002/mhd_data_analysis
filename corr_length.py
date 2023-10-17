import numpy as np
import glob
import re

def extract_number(filename):
    # Extract the number from the filename using a regex
    match = re.search(r'_cnt_(\d+)_', filename)
    return int(match.group(1)) if match else None

def compute_magnetic_correlation_length(filename):
    # Load the data from the file
    data = np.loadtxt(filename, usecols=(1, 14),skiprows = 4)
    
    # Extract k and power spectra values
    k_values = data[:, 0]
    power_spectra = data[:, 1]
    
    # Calculate the integrals in the numerator and denominator
    numerator = np.trapz(k_values**(-1) * power_spectra, k_values)
    denominator = np.trapz(power_spectra, k_values)
    
    # Avoid division by zero
    if denominator == 0:
        return None
    
    # Compute the magnetic correlation length
    correlation_length = numerator / denominator
    
    return correlation_length

# Get the list of files matching the pattern
files = glob.glob('Turb_hdf5_plt_cnt_????_spect_mags.dat')

files.sort(key=extract_number)
corr_length =[]

# Compute and print the magnetic correlation length for each file
for file in files:
    correlation_length = compute_magnetic_correlation_length(file)
    if correlation_length is not None:
        print(f'Magnetic Correlation Length for {file}: {correlation_length}')
        
        corr_length.append(correlation_length)
    else:
        print(f'Error in computing Magnetic Correlation Length for {file}')

np.savetxt('corr_length.txt',corr_length)
time = np.loadtxt(r'extracted_data.txt')

import matplotlib.pyplot as plt

plt.loglog(time[:len(corr_length)],corr_length)

plt.savefig('corrlength.pdf')
