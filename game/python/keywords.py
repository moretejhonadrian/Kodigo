import pke
import string
from nltk.corpus import stopwords
import spacy

import sys
import json
import os

def keywords(text, n):
    out = []

    extractor = pke.unsupervised.MultipartiteRank()
    extractor.load_document(input=text, language='en')
    pos = {'PROPN', 'NOUN', 'VERB'}
    stoplist = list(string.punctuation)
    stoplist += stopwords.words('english')
    extractor.candidate_selection(pos=pos)
    # 4. build the Multipartite graph and rank candidates using random walk,
    #    alpha controls the weight adjustment mechanism, see TopicRank for
    #    threshold/method parameters.
    try:
        extractor.candidate_weighting(alpha=1.1,
                                      threshold=0.75,
                                      method='average')
    except:
        return out

    keyphrases = extractor.get_n_best(n)

    for key in keyphrases:
        out.append(key[0])

    return out
    
def tag_word(keywords, keyword):
  nlp = spacy.load('en_core_web_sm')

  doc = nlp(keywords)

  for token in doc:
    if token.text.lower() == keyword.lower():
      return token.pos_

def clean_keywords(keywords):
    for i in range(len(keywords)):
        if ' ' in keywords[i]:
            phrase = keywords[i].split()
            key_tags = []
            for word in phrase:
                key_tags.append(tag_word(keywords[i], word))
            if len(key_tags) < 4:
                if key_tags == ['VERB', 'NOUN', 'NOUN']:
                    phrase.pop(0)
                    keywords[i] =  ' '.join(phrase)
                if key_tags == ['NOUN', 'NOUN', 'VERB']:
                    phrase.pop(2)
                    keywords[i] =  ' '.join(phrase)
                if key_tags == ['NOUN', 'VERB']:
                    phrase.pop(1)
                    keywords[i] =  ' '.join(phrase)
                if key_tags == ['VERB', 'NOUN', 'VERB']:
                    phrase.pop(2)
                    keywords[i] =  ' '.join(phrase)
            else:
                if key_tags[0] == 'VERB':
                    phrase.pop(0)
                    keywords[i] =  ' '.join(phrase)
                    continue
                for j in range(len(key_tags)):
                    if key_tags[j] == 'VERB':
                        phrase = phrase[:j]
                        keywords[i] =  ' '.join(phrase)
                        break

    return keywords

fn = sys.argv[1]
text = sys.argv[2]
n = int(sys.argv[3])
print(clean_keywords(keywords(text, n)))