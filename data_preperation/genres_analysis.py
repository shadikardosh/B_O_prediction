import pandas as pd
train_set = pd.read_csv('../data/train.csv')
print(train_set["genres"][1])