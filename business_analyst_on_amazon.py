# -*- coding: utf-8 -*-
"""Business Analyst on Amazon.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ddhq0t5__Ty-4ahLM3doRH52FgOKKVDj
"""

import pandas as pd
df = pd.read_csv('/content/cleaned_test.csv')
df.head()

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
file_path= '/content/drive/My Drive/Colab Notebooks/cleaned_test.csv'
df = pd.read_csv('/content/cleaned_test.csv')
df.head()

import csv

with open('cleaned_test.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

from google.colab import drive
drive.mount("/content/drive", force_remount = True)

import pandas as pd
file_path= '/content/drive/My Drive/Colab Notebooks/cleaned_test.csv'
df = pd.read_csv('/content/cleaned_test.csv')
df.head()

