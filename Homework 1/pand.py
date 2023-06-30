#!/usr/bin/env python

import pandas as pd

raw = pd.read_csv('AB_NYC_2019.csv')
df = raw.iloc[:, [9]]

var = df[df.notnull()].var(ddof=0)
mean = df[df.notnull()].mean()

print(mean)
print(var)