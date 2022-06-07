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

df.to_csv('./new_labels.csv', index=False)

#--------------------------------------------------
# split the dataset with 0.2 data test
#--------------------------------------------------
train, test = train_test_split(df, test_size=0.2)
train.to_csv('./train.csv', index=False)
test.to_csv('./test.csv', index=False)