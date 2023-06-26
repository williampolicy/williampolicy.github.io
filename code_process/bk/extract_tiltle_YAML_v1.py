import os
import datetime
from collections import Counter
from rake_nltk import Rake
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

import nltk
nltk.download('punkt')


def get_categories(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        
    vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
    X = vectorizer.fit_transform([content])
    freqs = zip(vectorizer.get_feature_names(), X.toarray()[0])    
    words = sorted(freqs, key=lambda x: -x[1])

    r = Rake()
    r.extract_keywords_from_text(content)
    phrases = r.get_ranked_phrases()[:10]  # Get top 10 keyword phrases

    return [word[0] for word in words[:5]], phrases  # Get top 5 frequent words

def update_blog(file_name):
    categories, key_phrases = get_categories(file_name)
    print("Most frequent categories:", categories)
    print("Key phrases:", key_phrases)

    with open(file_name, 'r', encoding='utf-8') as f:
        blog_content = f.read()

    title = " ".join(key_phrases[0].split()[:5])  # Using first key phrase as title
    today = datetime.date.today()
    new_file_name = today.isoformat() + "_" + "_".join(title.split()) + ".md"
    
    header = f"""---
layout: post
title:  "{title}"
date:   {today.isoformat()}
categories: {categories}
---

"""
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(blog_content)

    print(f"Updated blog saved to {new_file_name}")

if __name__ == "__main__":
    update_blog("blog_temp.md")
