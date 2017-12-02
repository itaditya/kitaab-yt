# coding: utf-8

# In[3]:


import numpy as np
from sklearn.preprocessing import normalize
import requests
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


class WikiEmbedding:

    def __init__(self, fname):

        self.w2idx = {}
        self.idx2w = []

        with open(fname, 'rb') as f:

            m, n = next(f).decode('utf8').strip().split(' ')
            self.E = np.zeros((int(m), int(n)))

            for i, l in enumerate(f):
                l = l.decode('utf8').strip().split(' ')
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


# In[2]:


get_ipython().system('sudo pip3 install matplotlib')


# In[5]:


en_embedding = WikiEmbedding('2016-09-01_2016-09-30_wikidata_100')


# In[9]:


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


# In[15]:


en_embedding.most_similar('keyword',min_similarity=0.5)


# In[12]:


from getting_started_helpers import get_tsne, plot_tsne


# In[13]:


tsne_en_embedding = get_tsne(en_embedding, pca_dim = 10, n_items=5000)
plot_tsne(en_embedding, tsne_en_embedding, n = 20)


# In[14]:


def items_to_titles(items, lang):
    lang += 'wiki'
    payload = {'action': 'wbgetentities',
               'props': 'sitelinks/urls',
               'format': 'json',
               'ids': '|'.join(items),
              }
    r = requests.get('https://www.wikidata.org/w/api.php', params=payload).json()

    return parse_wikidata_sitelinks(r, lang, True)


def titles_to_items(titles, lang):
    lang += 'wiki'
    payload = {'action': 'wbgetentities',
               'props': 'sitelinks/urls',
               'format': 'json',
               'sites': lang,
               'titles': '|'.join(titles),
              }
    r = requests.get('https://www.wikidata.org/w/api.php', params=payload).json()

    return parse_wikidata_sitelinks(r, lang, False)


def parse_wikidata_sitelinks(response, lang, item_to_title):

    d = {}
    if 'entities' not in response:
        print ('No entities in reponse')
        return d

    for item, v in response['entities'].items():
        if 'sitelinks' in v:
            if lang in v['sitelinks']:
                title = v['sitelinks'][lang]['title'].replace(' ', '_')
                if item_to_title:
                    d[item] = title
                else:
                    d[title] = item
    return d


# In[16]:


def most_similar(embedding, title, lang, n=10, min_similarity=0.7):
    item = titles_to_items([title,], lang)[title]
    nn = embedding.most_similar(item, n=n, min_similarity=min_similarity)
    nn_items = [x[0] for x in nn]
    nn_items_to_titles = items_to_titles(nn_items, lang)
    return [(nn_items_to_titles[x[0]], x[1]) for x in nn if x[0] in nn_items_to_titles]


# In[18]:


wikidata_embedding = WikiEmbedding('2016-09-01_2016-09-30_wikidata_100')


# In[22]:


import nltk
    essays = txt
    tokens = nltk.word_tokenize(essays)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word,pos in tagged         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos =='VBG' or pos == 'VB' or pos == 'JJR' or pos == 'JJ' )]
    downcased = [x.lower() for x in nouns]
    joined = " ".join(downcased)
    into_string = str(nouns)



# In[27]:


c=[]


# In[28]:


for i in b:
    essays = i
    tokens = nltk.word_tokenize(essays)
    tagged = nltk.pos_tag(tokens)
    nouns = [word for word,pos in tagged         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos =='VBG' or pos == 'VB' or pos == 'JJR' or pos == 'JJ' )]
    downcased = [x.lower() for x in nouns]
    joined = " ".join(downcased)
    c.append(joined.split(' '))
    #into_string = str(nouns)


# In[30]:


c[0]


# In[31]:


d=[]