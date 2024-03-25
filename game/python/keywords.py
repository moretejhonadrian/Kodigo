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