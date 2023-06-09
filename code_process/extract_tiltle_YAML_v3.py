import os
import re
import datetime
import nltk
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
    """
    Extracts the categories for the blog based on its content
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().lower()
        data = re.sub('[^a-zA-Z]', ' ', data)  # remove non-alphabetical characters
    
    # Apply TF-IDF  # change to 1.0
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
    """
    Extracts the title from the first line of the file
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        title = file.readline().strip()
    return title.replace('#', '')  # remove '#' from title

def update_blog(file_name):
    """
    Updates the blog by adding the YAML front matter
    """
    categories = get_categories(file_name)
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    title = get_title(file_name).replace(" ", "_")
    yaml_front_matter = f"---\nlayout: post\ntitle:  \"{title}\"\ndate:   {date}\ncategories: {categories}\n---\n"
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    updated_content = yaml_front_matter + content
    new_file_name = f"{date}_{title}.md".replace('__', '_')
    with open(new_file_name, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f"Updated blog saved to {new_file_name}")

# Run the program
update_blog("blog_temp.md")
