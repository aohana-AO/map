import pandas as pd
hoge = pd.read_csv('zenkoku.csv')

# データフレーム型に格納
df = pd.DataFrame(hoge)

#重複を確認
df.duplicated()

#重複を削除
sindf = df.drop_duplicates(subset='市区町村CD')


# CSVで保存
sindf.to_csv('zenkoku2.csv', index=False, encoding='utf-8-sig')