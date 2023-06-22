

import os
import re

version_file_path = "version.txt"
commit_message = input("Enter commit message: ")

# Check if version.txt exists, create it if it doesn't
if not os.path.exists(version_file_path):
    with open(version_file_path, 'w') as f:
        f.write("V.0.1")


# 读取版本文件
with open(version_file_path, 'r') as f:
    version = f.read().strip()

# 从版本号中提取数字
version_number = int(re.search(r'\d+$', version).group())

# 版本号加一
new_version_number = version_number + 1

# 更新版本文件
with open(version_file_path, 'w') as f:
    f.write(f"V.0.{new_version_number}")

# 执行git命令
os.system("git add -A")
os.system(f'git commit -m "V.0.{new_version_number} - {commit_message}"')
os.system("git push")

print(f"Commited Version V.0.{new_version_number}")


# import os
# import subprocess


# def get_version():
#     if os.path.isfile("version.txt"):
#         with open("version.txt", "r") as file:
#             return int(file.read())
#     else:
#         with open("version.txt", "w") as file:
#             file.write('0')
#         return 0

# def increment_version(version):
#     with open("version.txt", "w") as file:
#         file.write(str(version))
#     return version

# def git_commit(version, message):
#     subprocess.run(["git", "add", "-A"])
#     subprocess.run(["git", "commit", "-m", f"Version {version}: {message}"])
#     subprocess.run(["git", "push"])

# def main():
#     message = input("Enter the commit message: ")
#     version = get_version()
#     version += 1
#     increment_version(version)
#     git_commit(version, message)

# if __name__ == "__main__":
#     main()


