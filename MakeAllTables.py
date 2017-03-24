__author__ = 'Chris Connor'
import pandas as pd
import os
pd.set_option('display.max_rows', 10000)
# pd.options.display.float_format = '{:,.2f}%'.format
path = os.getcwd()
os.chdir(path)

df = pd.read_csv('Sheet_1_clean_nocommas.csv')
prevYears = df.loc[df[r'Please_indicate_your_Bosque_School_graduating_class_year_using_all_4_digits.'] <= 2012]
last5 = df.loc[df[r'Please_indicate_your_Bosque_School_graduating_class_year_using_all_4_digits.'] >= 2012]
x= [prevYears,last5]
y = ['prevYears', 'last5']
i = 0
for frame in x:
    filename = "%s.csv" %y[i]
    with open(filename, 'w') as f:
        for c in frame:
            valueList = frame[c].value_counts(normalize=True)
            f.write(str(valueList))
            f.write("\n")
    i+=1

