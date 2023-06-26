#!/usr/bin/env python3
import os
import re
import datetime
import argparse


def main():
    parser = argparse.ArgumentParser(description="This script handles versioning and git commit operations. The version number is stored in a text file, incremented, and then a new entry with the version number, a user-provided commit message, the user name, and the current timestamp is appended. These details are also used in the git commit message.")
    parser.add_argument('-m', '--commit_message', type=str, help='Specify the commit message that will be used in both the version text file and the git commit. If not provided, the script will prompt for it.')
    args = parser.parse_args()

    version_file_path = "version.txt"

    if args.commit_message:
        commit_message = args.commit_message
    else:
        commit_message = input("Enter commit message: ")

    if not os.path.exists(version_file_path):
        with open(version_file_path, 'w') as f:
            f.write("V.0.1\n")

    with open(version_file_path, 'r') as f:
        content = f.readlines()
        version = "V.0.1"
        for line in reversed(content):
            if line.strip().startswith("V.0."):
                version = line.strip()
                break

    version_number = int(re.search(r'\d+(?=\s|$)', version).group())
    new_version_number = version_number + 1
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d')

    with open(version_file_path, 'a') as f:
        f.write(f"V.0.{new_version_number} - {commit_message}  ©KANG - {timestamp}  \n")

    os.system("git add -A")
    os.system(f'git commit -m "V.0.{new_version_number} - {commit_message}  ©KANG - {timestamp} "')
    os.system("git push")

    print(f"Committed Version V.0.{new_version_number}")


if __name__ == "__main__":
    main()
