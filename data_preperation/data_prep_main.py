import numpy as np
import pandas as pd



train = pd.read_csv('../data/train.csv')
test = pd.read_csv('../data/test.csv')

print(train.columns)
print(train)
print(test)