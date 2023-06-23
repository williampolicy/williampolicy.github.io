import os
import re

version_file_path = "version.txt"
commit_message = input("Enter commit message: ")

# Check if version.txt exists, create it if it doesn't
if not os.path.exists(version_file_path):
    with open(version_file_path, 'w') as f:
        f.write("V.0.1\n")

# Read previous version and commit history
with open(version_file_path, 'r') as f:
    content = f.readlines()
    version = content[0].strip()
    commit_history = content[1:]

# Extract version number
version_number = int(re.search(r'\d+$', version).group())

# Increment version number
new_version_number = version_number + 1

# Update version file
with open(version_file_path, 'a') as f:
    f.write(f"V.0.{new_version_number}\n")
    f.write(f"V.0.{new_version_number} - {commit_message}\n")

# Execute git commands
os.system("git add -A")
os.system(f'git commit -m "V.0.{new_version_number} - {commit_message}"')
os.system("git push")

print(f"Committed Version V.0.{new_version_number}")
    