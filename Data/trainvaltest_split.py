# -*- coding: utf-8 -*-
"""trainvaltest_split

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/192FdadwvEyq9vUUEm4m3eGmtiZ9zv9TV
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

"""data load"""

original = pd.read_excel('/content/drive/MyDrive/프로젝트NLP/original_data.xlsx')
original = original.rename(columns = {'Customer_Description': 'text'})

X = original['text']
y = original['y']

X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.1, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.1/0.9, stratify=y_train_val, random_state=42)

train = pd.concat([X_train, y_train], axis=1)
val = pd.concat([X_val, y_val], axis=1)
test = pd.concat([X_test, y_test], axis=1)

train.to_excel('/content/drive/MyDrive/프로젝트NLP/train_원본.xlsx', index=False)
val.to_excel('/content/drive/MyDrive/프로젝트NLP/val.xlsx', index=False)
test.to_excel('/content/drive/MyDrive/프로젝트NLP/test.xlsx', index=False)