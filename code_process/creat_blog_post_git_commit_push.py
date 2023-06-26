#!/usr/bin/env python3
import os
import re
import datetime
import nltk
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
import string

nltk.download('stopwords')
nltk.download('punkt')

stopwords_list = nltk.corpus.stopwords.words('english')
stopwords_list += list(string.punctuation)
stopwords_list += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens if token not in stopwords_list]
    return tokens

def get_categories(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().lower()
        data = re.sub('[^a-zA-Z]', ' ', data)
    vectorizer = TfidfVectorizer(max_df=1.0, max_features=200000,
                                 min_df=0, stop_words=stopwords_list,
                                 use_idf=True, tokenizer=tokenize_text, ngram_range=(1,3))
    tfidf_matrix = vectorizer.fit_transform([data])
    feature_names = vectorizer.get_feature_names_out()
    dense = tfidf_matrix.todense()
    data_dense = dense[0].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(data_dense)), data_dense) if pair[1] > 0]
    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    phrases = []
    for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:5]:
        phrases.append(phrase)
    return phrases

def get_title(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        title = file.readline().strip()
    return title.replace('#', '').strip()  # strip any leading or trailing white spaces

def create_blog_post(file_name):
    categories = get_categories(file_name)
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    title = get_title(file_name)
    yaml_front_matter = f"---\nlayout: post\ntitle:  \"{title}\"\ndate:   {date}\ncategories: {categories}\n---\n"
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    updated_content = yaml_front_matter + content
    new_file_name = f"{date}-{title.replace(' ', '-')}.md".replace('--', '-')
    posts_dir = "/Users/kang/1.live_wit_GPT4/williampolicy.github.io/_posts/"
    with open(os.path.join(posts_dir, new_file_name), 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f"Updated blog saved to {os.path.join(posts_dir, new_file_name)}")

def commit_version_to_git(commit_message):
    version_file_path = "version.txt"
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

def main():
    parser = argparse.ArgumentParser(description="This script preprocesses a blog document, commits it to git, and keeps a version record.")
    parser.add_argument('file_name', type=str, help='Specify the blog file to be processed.')
    parser.add_argument('-m', '--commit_message', type=str, help='Specify the commit message that will be used in both the version text file and the git commit. If not provided, the script will prompt for it.')
    args = parser.parse_args()
    if not args.commit_message:
        args.commit_message = input("Enter commit message: ")
    create_blog_post(args.file_name)
    commit_version_to_git(args.commit_message)

if __name__ == "__main__":
    main()
