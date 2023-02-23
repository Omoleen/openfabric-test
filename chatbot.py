import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pandas as pd
import numpy as np
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import OrderedDict
import pickle
import nltk
nltk.download('popular')

data = pd.read_csv('total.csv')
stopwords_list = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def custom_tokenizer(doc):
    doc = doc.lower()
    words = word_tokenize(doc)
    pos_tags = pos_tag(words)

    non_stopwords = [w for w in pos_tags if not w[0].lower() in stopwords_list]

    non_punctuation = [w for w in non_stopwords if not w[0] in string.punctuation]

    lemmas_temp = []
    lemmas = []
    for w in non_punctuation:
        if w[1].startswith('J'):
            pos = wordnet.ADJ
        elif w[1].startswith('V'):
            pos = wordnet.VERB
        elif w[1].startswith('N'):
            pos = wordnet.NOUN
        elif w[1].startswith('R'):
            pos = wordnet.ADV
        else:
            pos = wordnet.NOUN

        lemmas_temp.append(lemmatizer.lemmatize(w[0], pos))

    for item in lemmas_temp:
        remove_repeats = (' '.join(OrderedDict.fromkeys(item.split())))
        lemmas.append(remove_repeats)

    return lemmas


tfidf_vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer)
tfidf_matrix = tfidf_vectorizer.fit_transform(tuple(data['question']))


class ChatBot:

    def clean(self):
        self.data = data.dropna()
        self.data = self.data.drop_duplicates(subset='question')
        self.data.to_csv('total.csv', index=False)
        self.data['answer'] = self.data['answer'].apply(lambda x: x.lower())
        self.data['answer'] = self.data['answer'].str.strip(".")
        self.data['question'] = self.data['question'].str.strip()
        self.data.head()

    def helper(self, question):
        query_vect = tfidf_vectorizer.transform([question])
        similarity = cosine_similarity(query_vect, tfidf_matrix)
        index_similarity = np.argmax(similarity, axis=None)

        return similarity, index_similarity

    def ask(self, question):
        question = question.lower()
        similarity, index_similarity = self.helper(question)

        if similarity[0, index_similarity] > 0.3:
            return data.iloc[index_similarity]['answer']
        else:
            return "I do not understand"
