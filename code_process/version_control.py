#!/usr/bin/env python3

import os
import re
import datetime

def main():
    version_file_path = "version.txt"
    commit_message = input("Enter commit message: ")

    # Check if version.txt exists, create it if it doesn't
    if not os.path.exists(version_file_path):
        with open(version_file_path, 'w') as f:
            f.write("V.0.1\n")

    # Read previous version and commit history
    with open(version_file_path, 'r') as f:
        content = f.readlines()
        # Initialize version as default
        version = "V.0.1"
        # Start from the last line and move upwards
        for line in reversed(content):
            # If this line looks like a version number, use it and stop
            if line.strip().startswith("V.0."):
                version = line.strip()
                break

    # Extract version number
    version_number = int(re.search(r'\d+(?=\s|$)', version).group())

    # Increment version number
    new_version_number = version_number + 1

    # Get current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d')

    # Update version file
    with open(version_file_path, 'a') as f:
        f.write(f"V.0.{new_version_number} - {commit_message}  ©KANG - {timestamp}  \n")

    # Execute git commands
    os.system("git add -A")
    os.system(f'git commit -m "V.0.{new_version_number} - {commit_message}  ©KANG - {timestamp} "')
    os.system("git push")

    print(f"Committed Version V.0.{new_version_number}")

if __name__ == "__main__":
    main()
