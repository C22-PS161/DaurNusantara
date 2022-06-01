import pandas as pd
from sklearn.model_selection import cross_val_predict, StratifiedKFold, train_test_split

#--------------------------------------------------
# read csv dataset from path
#--------------------------------------------------
DATASET_PATH = "./labels.csv"
df = pd.read_csv(DATASET_PATH)

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