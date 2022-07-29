import pandas as pd
import numpy as np

n_gram_string_list = []
excel_2_gram_probabilities_list = []
excel_3_gram_probabilities_list = []
empty_2_gram_list = []
empty_3_gram_list = []

df_N_gram_2 = pd.read_csv("/Users/cvkrishnarao/Desktop/RA/n_gram_data_converted/n_gram_coca_x2w_utf_8.csv")
df_N_gram_3 = pd.read_csv("/Users/cvkrishnarao/Desktop/RA/n_gram_data_converted/n_gram_coca_x3w_utf_8.csv")

n_gram_value = 2
test_string = "hi this is ratan sai rohith sexy boy"
x = [test_string.lower() for word in test_string.split()][0]
x = x.split()

for i in range(len(x)):
    y = x[i:i + n_gram_value]
    if len(y) == n_gram_value:
        n_gram_string_list.append(y)

if n_gram_value == 2:
    for i in n_gram_string_list:
        query_dataframe_2_gram = df_N_gram_2.loc[(df_N_gram_2['Word_One'] == i[0]) & (df_N_gram_2['Word_Two'] == i[1])]
        excel_2_gram_probabilities_list.append(query_dataframe_2_gram.values.tolist())
    print(excel_2_gram_probabilities_list)

elif n_gram_value == 3:
    for i in n_gram_string_list:
        query_dataframe_3_gram = df_N_gram_3.loc[(df_N_gram_3['Word_One'] == i[0]) & (df_N_gram_3['Word_Two'] == i[1]) & (df_N_gram_3['Word_Three'] == i[2])]

        if query_dataframe_3_gram is not None:
            excel_3_gram_probabilities_list.append(query_dataframe_3_gram.values.tolist())
        else:
            # Need to append the List for No Query Result
            pass

    print(excel_3_gram_probabilities_list)