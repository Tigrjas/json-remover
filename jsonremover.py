# Script that removes all json files in a folder
from pathlib import Path
import os

# Get the folder directory
p = Path.cwd()

# Create the Glob object in a list with only json files
list_json_glob = list(p.glob('*.json'))

# Sort through the list and delete each json file
for json in list_json_glob:
    os.remove(json)