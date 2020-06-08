import pandas
from pandas import DataFrame
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from csv import DictReader


#create a data frame with pandas
df = pandas.read_csv("template.csv")



# with the help of https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/
# create two lists called column_names and row_names
with open('template.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = DictReader(read_obj)

    # get column names from a csv file
    column_names = csv_dict_reader.fieldnames
    print(column_names)

    # get row names from a csv file
    row_names = []
    for row in csv_dict_reader:
        row_names.append(row[''])
    print(row_names)

#the names of the attributes
# rowNames = []
#the names of the peopel
# columnNames = []

#rowNames but not the last one
# X = df[rowNames]
#only the last entry of row names
# y = df['crush index']

# X = sm.add_constant(X) # adding a constant

# model = sm.OLS(Y, X).fit()
# predictions = model.predict(X) 
# print_model = model.summary()
# print(print_model)

#use adjusted r square value
#you should be able to find the p value based off of this

#throw equation into array.. or figure out how to plug stuff in
#import another spreadsheet where you can put the same data
