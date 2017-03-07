# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:18:16 2017

@author: saurabh.s1
"""


from logistic_regression_cv import logistic_regression_cv
from utils import load_meta
from utils import fetch_posts
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

score_thershold = 0
C = 10
cv_n_folds = 10
train_errors = []
test_errors = []


#bias,variance curves
C = .1
del train_errors[:]
del test_errors[:]
post_class = np.asarray([meta[aid]['Score'] > score_thershold for aid in all_answers])
total_dataset_size = 2400
_range = range(100,total_dataset_size,10)
for dataset_size in _range:
    train_error, test_error = logistic_regression_cv(post_features, post_class, C, cv_n_folds, length_dataset = dataset_size)
    train_errors.append(train_error)
    test_errors.append(test_error)    


fig,ax = plt.subplots()
ax.plot(_range, train_errors, 'r-',label = "train_error")
ax.plot(_range, test_errors, 'g-',label = "test_error")
legend = ax.legend(loc = "upper center")
plt.xlabel('Dataset_size')
plt.ylabel('Errors')
plt.title('Bias Vs Variance - lr, C = {}, score_threshold = {}, dataset_size = {}'.format(C, score_thershold, total_dataset_size))
plt.savefig('Bias Vs Variance - lr, C = {}, score_threshold = {}, dataset_size = {}.png'.format(C, score_thershold, total_dataset_size))
plt.show()

#precision vs recall curve 
#C = .01
#cv_n_folds = 2
#post_class = np.asarray([meta[aid]['Score'] > score_thershold for aid in all_answers])
#dataset_size = 2400
#train_error, test_error, precision, recall, thresholds = logistic_regression_cv(post_features, post_class, C, cv_n_folds, length_dataset = dataset_size, pr = True, dump = True)
#print train_error, test_error
#
#score_thershold = 0   
#fig,ax = plt.subplots()
#ax.plot(recall, precision, 'r-',label = "p/r")
#legend = ax.legend(loc = "upper center")
#plt.xlabel('recall')
#plt.ylabel('precision')
#plt.ylim(0.75, 1.05)
#plt.title('P/R - lr, C = {}, score_threshold = {}, dataset_size = {}'.format(C, score_thershold, dataset_size))
#plt.savefig('PR - lr, C = {}, score_threshold = {}, dataset_size = {}.png'.format(C, score_thershold, dataset_size))
#plt.show()
 
