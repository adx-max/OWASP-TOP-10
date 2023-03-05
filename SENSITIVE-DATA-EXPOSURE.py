print('SENSITIVE DATA EXPOSURE SCRIPT, CREATED BY ANESTUS UDUME FROM BENTECH SECURITY')
#!/usr/bin/env python3

import os
import re

# Define the regex pattern to search for sensitive data
sensitive_pattern = r'\b(?:password|secret|key|access_token)\b'

# Define the directories and files to search
search_paths = ['/path/to/directory', '/path/to/file.txt']

# Define a function to recursively search for the pattern within the specified directory or file
def search_for_sensitive_data(path):
    if os.path.isfile(path):
        # If the path is a file, search for the pattern within the file
        with open(path, 'r') as f:
            content = f.read()
            if re.search(sensitive_pattern, content, re.IGNORECASE):
                print(f"Sensitive data found in file: {path}")
    elif os.path.isdir(path):
        # If the path is a directory, recursively search for the pattern within all files in the directory
        for subdir, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(subdir, file)
                search_for_sensitive_data(file_path)

# Search for sensitive data within the specified directories and files
for path in search_paths:
    search_for_sensitive_data(path)
