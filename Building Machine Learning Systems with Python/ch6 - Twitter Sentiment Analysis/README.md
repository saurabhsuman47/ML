The project is about sentiment analysis of twitter data. 

The goal is to build a simple sentiment classifier of tweets.(ie classify tweets as negative or positive).

It uses the dataset: https://raw.githubusercontent.com/zfz/twitter_corpus/master/full-corpus.csv for traing and testing.
Only tweets with positive or negative sentiments have been considered.

The model is a pipeline of:
1) TfIdf vectorizer - generate tfidf values from tweet text which can be used by the classifier.
2) Naive Bayes Classifier - from tfidf vectors predicts positive or negative class.
For finding the best parameters for the estimator GridSearchCV has been used.

The model is trained using ShuffleSplit cross-validation.
The results are following:
	Train Accuracy = 0.958453473132
	Test Accuracy = 0.818902439024
	Precision Recall Area Under Curve = 0.882747452315

Contents:
1) full-corpus.csv - contains the dataset with the following attributes for each tweet : "Topic","Sentiment","TweetId","TweetDate","TweetText"
2) load_data.py - contains function that loads the data from full-corpus to numpy arrays
3) model.py - contains a)function for creating a pipeline model of tfidf vectorizer and naive bayes classifier, b) function for training and testing the model
4) main.py - code for finding best parameters for model using GridSearchCV , calls other functions
5) clf.dat - best classifier is saved as .dat file(no need to train again)
6) PR - pos-neg.png - Precison-recall curve when classifying positive or negative.



