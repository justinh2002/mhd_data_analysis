import os
import random

def randomize_flash_par_seed(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'st_MagneticSeed' in line:
            new_seed = random.randint(0, 1000000)
            lines[i] = f'st_MagneticSeed = {new_seed}\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

# List of subdirectory names
subdirectories = ['seed1', 'seed2', 'seed3', 'seed4', 'seed5', 'seed6', 'seed7', 'seed8', 'seed9', 'seed10','seed11', 'seed12', 'seed13', 'seed14', 'seed15', 'seed16', 'seed17', 'seed18', 'seed19', 'seed20']

# Process flash.par files in each subdirectory
for directory in subdirectories:
    dir_path = os.path.join(os.getcwd(), directory)
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            if file_name == 'flash.par':
                file_path = os.path.join(root, file_name)
                randomize_flash_par_seed(file_path)
                print(f"Randomized st_MagneticSeed in {file_path}")
