# file = open('datacf (3).txt')
# for cheese in file:
#     print(cheese)

# file = open('datacf (3).txt')
# count = 0
# for line in file:
#     count = count + 1
# print('Line Count:', count)

# for i in [2, 4, 5, 6,]:
#     print(i)
#     print('hello')

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year:',  friend)
# print('Done!')
#
# print(friends[1])

# total = 0
# count = 0
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#
# average = total / count
# print('Average:', average)

# numlist = list()
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist) / len(numlist)
# print('Average:', average)

# import pandas as pd
# import openpyxl
# import pprint
# wb = openpyxl.load_workbook('datacf (3).txt')
# data= pd.read_excel('datacf (3).txt')
# print(wb)
# print(data)





#
# ['Sheet1']
# sheet = wb['Sheet1']
# cellA2 = sheet['B2']
# cell = sheet.cell(row=2, column=2,)
# print(cell.value)







import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
dataset = pd.read_csv('datacf (3).txt')



