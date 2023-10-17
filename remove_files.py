import os
import glob

# Define the pattern to match
pattern = "Turb_hdf5_chk_*"

# Loop through subdirectories seed1 to seed10
for seed_dir in range(1, 11):
    subdirectory = f"seed{seed_dir}"
    
    # Check if the subdirectory exists
    if os.path.exists(subdirectory) and os.path.isdir(subdirectory):
        print(f"Removing {pattern} files in {subdirectory}...")
        
        # Use glob to find files matching the pattern in the subdirectory
        files_to_remove = glob.glob(os.path.join(subdirectory, pattern))
        
        # Remove the matched files
        for file_path in files_to_remove:
            os.remove(file_path)
            print(f"Removed {file_path}")
    else:
        print(f"Directory {subdirectory} not found.")

print("File removal completed.")
