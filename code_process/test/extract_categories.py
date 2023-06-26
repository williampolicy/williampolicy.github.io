from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens

def get_categories(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()

    # 你可以根据需要更改这里的参数
    vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words=stopwords.words('english'),
                                 use_idf=True, tokenizer=tokenize_text, ngram_range=(1,3))

    tfidf_matrix = vectorizer.fit_transform([data])
    feature_names = vectorizer.get_feature_names()

    dense = tfidf_matrix.todense()
    doc_phrase_scores = dense[0].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(doc_phrase_scores)), doc_phrase_scores) if pair[1] > 0]

    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    top_words = []
    for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
        top_words.append(phrase)

    print(f"Top categories: {top_words}")

get_categories("blog_temp.md")
