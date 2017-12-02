# coding: utf-8

# In[2]:

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

word_string = "asf afasf sdf  sdfa asf asf"
wordcloud = WordCloud(font_path='.local/share/fonts/sans-serif.ttf',
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(word_string)


plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# In[44]:

from nltk.corpus import stopwords


# In[49]:

len(stopwords.words('english'))


# In[21]:

STOPWORDS.add('let')


# In[167]:

len(STOPWORDS)


# In[12]:

from os import path


# In[ ]:

text = open('lhack.tsv').read()

wordcloud = WordCloud(background_color='white',stopwords=STOPWORDS,random_state=42).generate(joined)

import matplotlib.pyplot as plt

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
#plt.savefig('as123d.png')


# In[168]:

b


# In[102]:




# In[109]:

b


# In[13]:

a=[]
b=[]
with open('lhack.tsv') as f:
    for l in f:
        n=l.strip().split("\t")
        try:
        #a.append(n[0])
            if n[1]=='[Music]':
                continue
            else:
                a.append(n[0])
                b.append(n[1])
        except:
            pass
txt=''
for i in b:
    txt=txt+' '+i


# In[14]:

txt


# In[51]:

import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# change this to read in your data
finder = BigramCollocationFinder.from_words(
   nltk.corpus.genesis.words('english-web.txt'))

# only bigrams that appear 3+ times
finder.apply_freq_filter(3)

# return the 10 n-grams with the highest PMI
finder.nbest(bigram_measures.pmi, 10)


# In[55]:

import nltk
ngramlist=[]
raw=txt
x=1
ngramlimit=6
tokens=nltk.word_tokenize(raw)

while x <= ngramlimit:
    ngramlist.extend(nltk.ngrams(tokens, x))
    x+=1


# In[15]:

import nltk
essays = txt
tokens = nltk.word_tokenize(essays)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos =='VBG' or pos == 'VB' or pos == 'JJR' or pos == 'JJ' )]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased)
into_string = str(nouns)



# In[136]:

c=['see']


# In[137]:

ed = nltk.pos_tag(c)


# In[138]:

ed


# In[74]:

l=joined.decode()


# In[78]:

import nltk

text =txt

# Used when tokenizing words
sentence_re = r'''(?x)      # set flag to allow verbose regexps
      ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*            # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
    | \.\.\.                # ellipsis
    | [][.,;"'?():-_`]      # these are separate tokens
'''

lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()

#Taken from Su Nam Kim Paper...
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)

toks = nltk.regexp_tokenize(text, sentence_re)
postoks = nltk.tag.pos_tag(toks)

print (postoks)

tree = chunker.parse(postoks)

from nltk.corpus import stopwords
stopwords = stopwords.words('english')


def leaves(tree):
    for subtree in tree.subtrees(filter = lambda t: t.node=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    word = stemmer.stem_word(word)
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term

terms = get_terms(tree)

for term in terms:
    for word in term:
        print (word),
    print()


# In[83]:

from textblob import TextBlob, Word
import sys
import random

#text = sys.stdin.read().decode('ascii', errors="ignore")
blob = TextBlob(txt)

nouns = list()
for word, tag in blob.tags:
    if tag == 'NN':
        nouns.append(word.lemmatize())


for item in random.sample(nouns, 10):
    word = Word(item)
    print (word.pluralize())


# In[1]:

import numpy as np
from sklearn.preprocessing import normalize
import requests
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')
get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')


# In[6]:

class WikiEmbedding:

    def __init__(self, fname):

        self.w2idx = {}
        self.idx2w = []

        with open(fname, 'rb') as f:

            m, n = next(f).decode('latin-1').strip().split(' ')
            self.E = np.zeros((int(m), int(n)))

            for i, l in enumerate(f):
                l = l.decode('latin-1').strip().split(' ')
                w = l[0]
                self.E[i] = np.array(l[1:])
                self.w2idx[w] = i
                self.idx2w.append(w)

        self.E = normalize(self.E)
        self.idx2w = np.array(self.idx2w)

    def most_similar(self, w, n=10, min_similarity=0.5):


        if type(w) is str:
            w = self.E[self.w2idx[w]]

        scores = self.E.dot(w)
        min_idxs = np.where(scores > min_similarity)
        ranking = np.argsort(-scores[min_idxs])[1:(n+1)]
        nn_ws = self.idx2w[min_idxs][ranking]
        nn_scores = scores[min_idxs][ranking]
        return list(zip(list(nn_ws), list(nn_scores)))


# In[ ]:

en_embedding = WikiEmbedding('Downloads/2017-01-01_2017-01-30_en_100')


# In[ ]:

en_embedding.most_similar('Wikipedia')


# In[ ]:

a=[]
b=[]
with open('lhack.tsv') as f:
    for l in f:
        n=l.strip().split("\t")
        print(n[1])
        try:
        #a.append(n[0])
            if n[1]=='[Music]':
                continue
            else:
                a.append(n[0])
                b.append(n[1])
        except:
            pass
txt=''
for i in b:
    txt=txt+' '+i


# In[ ]:

a


# In[ ]:


    a=[]
    b=[]

    with open('lhack.tsv') as f:
        for l in f:
            n=l.strip().split("\t")
            print(n[1])
            try:
            #a.append(n[0])
                if n[1]=='[Music]':
                    continue
                else:
                    a.append(n[0])
                    b.append(n[1])
            except:
                pass
    txt=''
    for i in b:
        txt=txt+' '+i

    essays = txt
    tokens = nltk.word_tokenize(essays)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word,pos in tagged         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos =='VBG' or pos == 'VB' or pos == 'JJR' or pos == 'JJ' )]
    downcased = [x.lower() for x in nouns]
    joined = " ".join(downcased)
    into_string = str(nouns)



    wordcloud = WordCloud(background_color='white',stopwords=STOPWORDS,random_state=42).generate(joined)

    import matplotlib.pyplot as plt

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# In[3]:

STOPWORDS


# In[8]:

a=['file','and']


# In[9]:

STOPWORDS.add(a)