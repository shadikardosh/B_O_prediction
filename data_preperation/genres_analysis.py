import pandas as pd
pd.set_option('max_columns', None)
import numpy as np
import ast
import matplotlib.pyplot as plt
import pylab


def text_to_dict(df):
    for column in dict_columns:
        df[column] = df[column].apply(lambda x: {} if pd.isna(x) else ast.literal_eval(x))
    return df

train_set = pd.read_csv('../data/train.csv')

dict_columns = ['belongs_to_collection', 'genres', 'production_companies',
                'production_countries', 'spoken_languages', 'Keywords', 'cast', 'crew']

train_set = text_to_dict(train_set)

genre_names = set(x["name"] for l in train_set["genres"] for x in l)
for genre_name in genre_names:
    train_set["genre_name_"+genre_name] = [1 if genre_name in str(l) else 0
                                           for l in train_set["genres"]]

print(train_set.head(2))

train_set["number_of_genres"] = [len(l) for l in train_set["genres"]]

plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plt.scatter(train_set['number_of_genres'], train_set['revenue'])
plt.title('# genres vs revenue')
pass
