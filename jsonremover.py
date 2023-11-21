# Script that removes all json files in a folder and subfolders
from pathlib import Path
import os
import sys

# Helper function
def remove_json(directory):
    for json in directory:
        os.remove(json)

# Get the folder directory from command line
try:
    directory_name = sys.argv[1]
    directory = Path(directory_name)
    if directory.exists():
        for root, dirs, files, in os.walk(directory):
            sub_directory = Path(root)
            list_json_glob = list(sub_directory.glob('*.json'))
            remove_json(list_json_glob)
    else:
        print(f"The directory '{directory_name}' does not exist")
except:
    print("Please pass directory name as command line argument")
