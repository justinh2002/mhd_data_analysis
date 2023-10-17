import os

# Loop to create directories from seed1 to seed20
for i in range(1, 21):
    os.makedirs(f"seed{i}", exist_ok=True)
