import subprocess

def push_to_git(commit_message):
    posts_dir = "/Users/kang/1.live_wit_GPT4/williampolicy.github.io/_posts/"

    # 1. git add -A
    subprocess.check_output(['git', 'add', '-A'], cwd=posts_dir)
    print("Added all changes to git.")

    # 2. git commit -m "message"
    subprocess.check_output(['git', 'commit', '-m', commit_message], cwd=posts_dir)
    print(f"Commited changes with message: {commit_message}")

    # 3. git push
    result = subprocess.check_output(['git', 'push'], cwd=posts_dir)
    print(result.decode('utf-8'))
    print("Pushed changes to remote git repository.")

# Run the program
push_to_git("Updated blog post")
