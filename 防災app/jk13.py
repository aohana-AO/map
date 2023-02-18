import pandas as pd

X=pd.read_csv('災害csv/指定緊急避難所一覧2x.csv')
print(X.loc[1744,'管理者電話'])
X=X.replace('\n', '',regex=True)
print(X.loc[1744,'管理者電話'])
"""
x2=X.replace({'指定緊急避難場所との重複': {1: '〇'}})
X[X.指定緊急避難場所との重複==1]='〇'
for index, r in X.iterrows(): 
    if X.loc[index,'指定緊急避難場所との重複']=='1.0':
         X.loc[index,'指定緊急避難場所との重複']='〇'
    print(X.loc[index,'指定緊急避難場所との重複'])

print(X.指定緊急避難場所との重複)
print(x2.指定緊急避難場所との重複)
"""

X.to_csv('災害csv/指定緊急避難所一覧34.csv')