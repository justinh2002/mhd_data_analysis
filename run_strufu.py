import os

# Loop through seed directories from seed1 to seed10
for seed_num in range(1, 21):
    seed_dir = f'seed{seed_num}'
    
    # Check if the directory exists
    if os.path.isdir(seed_dir):
        job_script = os.path.join(seed_dir, 'run_strufu.sh')
        
        # Check if job.sh exists in the directory
        if os.path.isfile(job_script):
            # Change the working directory to the subdirectory
            os.chdir(seed_dir)
            
            # Use os.system to submit the job using qsub
            os.system('qsub run_strufu.sh')
            
            # Return to the parent directory
            os.chdir('..')
        else:
            print(f'run_strufu.sh not found in {seed_dir}')
    else:
        print(f'{seed_dir} not found')
