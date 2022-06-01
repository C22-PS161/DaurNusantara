import copy
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold, train_test_split

#--------------------------------------------------
# read csv dataset from path
#--------------------------------------------------
DATASET_PATH = "./labels.csv"
df = pd.read_csv(DATASET_PATH)

#--------------------------------------------------
# add classes number into dataframe
#--------------------------------------------------
# kantong           : 0 
# kertas            : 1 
# piring            : 2 
# sampah_organik    : 3 
# kardus            : 4 
# cup               : 5 
# kaleng            : 6 
# botol             : 7
targets_class = copy.deepcopy(df['class'])
arr_unique = targets_class.unique()

for i in range(len(arr_unique)):
    for j in range(len(targets_class)):
        if(targets_class.values[j] == arr_unique[i]):
            targets_class.values[j] = i

df['class_int'] = targets_class

#--------------------------------------------------
# split the dataset with 0.2 data test
#--------------------------------------------------
train, test = train_test_split(df, test_size=0.2)

#--------------------------------------------------
# split the feature and target
#--------------------------------------------------
y = df['class'].values
x = df.drop(['class'], axis=1)

y_train = train['class'].values
x_train = train.drop(['class'], axis=1)

y_test = test['class'].values
x_test = test.drop(['class'], axis=1)

#--------------------------------------------------
# modeling 
#--------------------------------------------------


#--------------------------------------------------
# cross validation performance model
#--------------------------------------------------
SPLIT_NUM = 10
skf = StratifiedKFold(n_splits=SPLIT_NUM, random_state=42, shuffle=True)

# predict the cross validation with kfold model
kfold_predict = cross_val_predict(clf, x, y, cv=skf)