# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:34:54 2017

@author: saurabh.s1
"""

from utils import load_meta
from utils import fetch_posts
from knn_cv import knn_cv
import matplotlib.pyplot as plt
import nltk
import numpy as np



#######
chosen = "chosen.tsv"
chosen_meta = "chosen-meta.json"
meta, id_to_idx, idx_to_id = load_meta(chosen_meta)
all_posts = list(meta.keys())
all_questions = [q for q, v in meta.items() if ('ParentId' in v.keys() and v['ParentId'] == -1)]
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
post_features = np.asarray([get_features(aid) for aid in all_answers])

n_neighbors = 8
n_folds = 10
score_thershold = 0
train_errors = []
test_errors = []

#bias,variance curves
n_neighbors = 10
del train_errors[:]
del test_errors[:]
post_class = np.asarray([meta[aid]['Score'] > score_thershold for aid in all_answers])
total_dataset_size = 2400
_range = range(100,total_dataset_size,10)
for dataset_size in _range:    
    train_accuracy, test_accuracy = knn_cv(post_features, post_class, n_folds, n_neighbors, dataset_size)
    train_errors.append(1-train_accuracy)
    test_errors.append(1-test_accuracy)

fig,ax = plt.subplots()
ax.plot(_range, train_errors, 'k-', label='train_error')
ax.plot(_range, test_errors, 'r-', label='test_error')
legend = ax.legend(loc='upper center', shadow=True)
plt.xlabel('Dataset_size')
plt.ylabel('Errors')
plt.title('Bias Vs Variance - knn, k = {}, score_threshold = {}, dataset_size = {}'.format(n_neighbors, score_thershold, total_dataset_size))
plt.savefig('Bias Vs Variance - knn, k = {}, score_threshold = {}, dataset_size = {}'.format(n_neighbors, score_thershold, total_dataset_size))
plt.show()
