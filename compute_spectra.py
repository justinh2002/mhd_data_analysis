import subprocess
import glob

# Get list of all files with the matching pattern
file_list = glob.glob('Turb_hdf5_plt_cnt_????')

# Extract numeric part from each file name and sort the list numerically
file_list_sorted = sorted(file_list, key=lambda x: int(x.split('_')[-1]))

# For each file in the sorted list, construct and run the mpirun command
for file_name in file_list_sorted:
    # Extract the file number from the file name (assuming it's at the end)
    file_number = file_name.split('_')[-1]
    
    # Construct the command
    cmd = ['mpirun', '-np', '144', 'spectra_mpi', file_name, '-types', '1', '2']
    
    # Set up the output file name
    output_file_name = f"{file_name}.out"
    
    # Open the output file in write mode
    with open(output_file_name, 'w') as outfile:
        # Run the command using subprocess and write its output to the file
        try:
            print(f"Running command: {' '.join(cmd)}")
            result = subprocess.run(cmd, check=True, stdout=outfile, stderr=outfile)
            print(f"Command Output written to: {output_file_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {e}")
            outfile.write(f"Error running command: {e}")
