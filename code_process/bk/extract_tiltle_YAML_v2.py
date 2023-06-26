import os
import re
import datetime
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from rake_nltk import Rake
import string

def clean_non_english(text):
    """
    Removes non-English characters from the text
    """
    return re.sub(r'[^\x00-\x7F]+', ' ', text)

def get_categories(file_name):
    """
    Extracts the categories for the blog based on its content
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        content = clean_non_english(file.read())
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(content.split())
    words = vectorizer.get_feature_names_out()
    frequencies = sum(X).toarray()[0]
    r = Rake(min_length=2, max_length=4)
    r.extract_keywords_from_text(content)
    key_phrases = r.get_ranked_phrases_with_scores()
    print(f"Most frequent categories: {words}")
    print(f"Key phrases: {key_phrases}")
    return words, key_phrases

def update_blog(file_name):
    """
    Updates the blog by adding the YAML front matter
    """
    categories, key_phrases = get_categories(file_name)
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    title = key_phrases[0][1].replace(" ", "_")
    yaml_front_matter = f"---\nlayout: post\ntitle:  \"{title}\"\ndate:   {date}\ncategories: {categories}\n---\n"
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    updated_content = yaml_front_matter + content
    new_file_name = f"{date}_{title}.md"
    with open(new_file_name, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f"Updated blog saved to {new_file_name}")

# Run the program
nltk.download('stopwords')
nltk.download('punkt')
update_blog("blog_temp.md")
