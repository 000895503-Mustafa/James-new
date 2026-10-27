import os

# Get the PATH folders
path_list = os.get_exec_path()

# Store unique folder names
unique_folders = []

for path in path_list:
    # Replace backslashes and split into parts
    parts = path.replace("\\", "/").split("/")

    # Check each folder name
    for folder in parts:
        if folder != "" and folder not in unique_folders:
            unique_folders.append(folder)

# Display results
print("The following", len(unique_folders),
      "unique folder names are found in my path:")

for folder in unique_folders:
    print(folder)
