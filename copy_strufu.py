import shutil
import os

def copy_files(destination_folder, file_names):
    source_folder = os.getcwd()  # Get current working directory as the source folder
    for file_name in file_names:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy(source_path, destination_path)
        print(f"Successfully copied {file_name} to {destination_folder}")

# Get the destination folder names as input from the user
input_folders = "seed1,seed2,seed3, seed4, seed5, seed6, seed7, seed8, seed9, seed10, seed11, seed12, seed13, seed14, seed15, seed16, seed17, seed18, seed19, seed20"
destination_folders = [folder.strip() for folder in input_folders.split(",")]

# List the names of the files to be copied
file_names = ["run_strufu.sh"]

# Copy the files to each specified destination folder
for folder in destination_folders:
    copy_files(folder, file_names)
