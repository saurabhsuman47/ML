# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 17:12:07 2017

@author: saurabh.s1
"""



from data import chosen, chosen_meta
from utils import load_meta
from utils import fetch_posts
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pickle
from sklearn.metrics import precision_recall_curve


#######


meta, id_to_idx, idx_to_id = load_meta(chosen_meta)
all_answers = [q for q, v in meta.items() if ('ParentId' in v.keys() and v['ParentId'] != -1)]
feature_names = np.array((
    'NumTextTokens',
    'NumCodeLines',
    'LinkCount',
    'AvgSentLen',
    'AvgWordLen',
    'NumAllCaps',
    'NumExclams',
    'NumImages'
))



def prepare_sent_features():
    for pid, text in fetch_posts(chosen, with_index=True):
        if not text:
            meta[pid]['AvgSentLen'] = meta[pid]['AvgWordLen'] = 0
        else:
            sent_lens = [len(nltk.word_tokenize(
                sent)) for sent in nltk.sent_tokenize(text)]
            meta[pid]['AvgSentLen'] = np.mean(sent_lens)
            meta[pid]['AvgWordLen'] = np.mean(
                [len(w) for w in nltk.word_tokenize(text)])

        meta[pid]['NumAllCaps'] = np.sum(
            [word.isupper() for word in nltk.word_tokenize(text)])

        meta[pid]['NumExclams'] = text.count('!')
prepare_sent_features()
def get_features(aid):
    return tuple(meta[aid][fn] for fn in feature_names)
    
clf = pickle.load(open("logreg.dat","r"))
post_features = np.asarray([get_features(aid) for aid in all_answers])
post_class = np.asarray([meta[aid]['Score'] > 0 for aid in all_answers])

def classify(clf,X):
    return 1/(1+np.exp(-(clf.intercept_ + np.dot(X, (clf.coef_).transpose()))))

errors = []
_range = range(50,12330,10)
for i in _range:
    x = post_features[:i]
    y = post_class[:i]
    y_predicted = classify(clf,x)
    errors.append(np.mean(abs(y.reshape(len(y),1) - y_predicted)))
    
fig,ax = plt.subplots()
ax.plot(_range, errors, 'r-',label = "test_error")
legend = ax.legend(loc = "upper center")
plt.xlabel('Dataset_size')
plt.ylabel('Testing_Error')
plt.title('Testing error vs dataset size - lr, C = {}, score_threshold = {}'.format(.1, 0))
plt.savefig('Testing error vs dataset size - lr, C = {}, score_threshold = {}.png'.format(.1, 0))
plt.show()


precision, recall, thresholds = precision_recall_curve(y, y_predicted)
fig,ax = plt.subplots()
ax.plot(recall, precision, 'r-',label = "p/r")
legend = ax.legend(loc = "upper center")
plt.xlabel('recall')
plt.ylabel('precision')
plt.ylim(0.75, 1.05)
plt.title('P/R - lr, generalize over testing data, C = {}, score_threshold = {}'.format(.1, 0))
plt.savefig('PR - lr, generalize over testing data, C = {}, score_threshold = {}.png'.format(.1, 0))
plt.show()