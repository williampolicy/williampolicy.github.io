
import os
import re
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import nltk
from nltk.corpus import stopwords
import string
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')

stopwords_list = stopwords.words('english')
stopwords_list += list(string.punctuation)
stopwords_list += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens if token not in stopwords_list]
    return tokens

def get_categories(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().lower()
        data = re.sub('[^a-zA-Z]', ' ', data)  # remove non-alphabetical characters
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
    for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
        phrases.append(phrase)
    print(f"Top categories: {phrases}")
    return phrases

get_categories("blog_temp.md")


# from sklearn.feature_extraction.text import TfidfVectorizer
# import nltk
# from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('stopwords')

# def tokenize_text(text):
#     tokens = nltk.word_tokenize(text)
#     tokens = [token.strip() for token in tokens]
#     return tokens

# def get_categories(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         data = file.read()

#     vectorizer = TfidfVectorizer(max_df=1.0, max_features=200000,
#                                  min_df=0, stop_words=stopwords.words('english'),
#                                  use_idf=True, tokenizer=tokenize_text, ngram_range=(1,3))

#     tfidf_matrix = vectorizer.fit_transform([data])
#     # feature_names = vectorizer.get_feature_names()
#     feature_names = vectorizer.get_feature_names_out()


#     dense = tfidf_matrix.todense()
#     doc_phrase_scores = dense[0].tolist()[0]
#     phrase_scores = [pair for pair in zip(range(0, len(doc_phrase_scores)), doc_phrase_scores) if pair[1] > 0]

#     sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
#     top_words = []
#     for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
#         top_words.append(phrase)

#     print(f"Top categories: {top_words}")


