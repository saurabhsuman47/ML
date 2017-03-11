The project is about predicting housing prices using regression. 

It uses the Boston Housing Prices Dataset for training and testing. The dataset is available in sklearn.datasets.
It is also available from http://archive.ics.uci.edu/ml/datasets/Housing.

Contents:

1. boston_housing_prices_dataset_description.txt - description of the dataset. There are 506 samples with 13 attributes and a target value.
2. main.py - entry point, loads data, trains model and generate Lasso and Ridge paths.
3. model.py - contains function for training and testing the model
4. plot.py - contains plotting functions
5. Regression over Boston data(Actual Values vs Predicted Values).png - visualization of actual vs predicted values
6. Regression over Boston data(Actual Values and Predicted Values for samples).png - visualization of actual vs predicted values
7. Lasso path(Coefficient weights vs Alpha).png - Coefficient weights vs Alpha for L1 regularization
8. Ridge path(Coefficient weights vs Alpha).png - Coefficient weights vs Alpha for L2 regularization

Main.py loads the data and uses it to train Linear Regression Model(available in sklearn.linear_model)
The model is trained using KFold cross-validation.
The results are following(without regularization):

* Train R2 score: 0.741841312823
* Test R2 score: 0.711632756616
* Root Mean Square Error: 4.67950630064

For regularization Lasso(L1 penalty), Ridge(L2 penalty) has been used.(available from sklearn.linear_model)
There is no significant improvement in R2 scores by using Lasso or Ridge(by training for different alphas). 

Finally Coefficients weight vs various alphas has been visualized for both models(Lasso and Ridge).
As the alpha increases, coefficient weight decreases significantly.





