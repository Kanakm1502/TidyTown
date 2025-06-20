import os

# Define the main directory
main_dir = 'dataset'

# Define the subdirectories
sub_dirs = ['clean', 'unclean']

# Create the main directory if it doesn't exist
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    print(f"Created directory: {main_dir}")

# Create the subdirectories
for sub_dir in sub_dirs:
    path = os.path.join(main_dir, sub_dir)
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Created directory: {path}")
