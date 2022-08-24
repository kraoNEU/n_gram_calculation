import pandas as pd
from bi_gram_calculation import cleanupString, n_gram_list, n_gram_probability_calculation

df = pd.read_csv("/Users/cvkrishnarao/Desktop/n_gram_document_copy.csv")
list_n_gram = list(df["SET 4"])


for n_gram in list_n_gram:
    x = cleanupString(n_gram)
    gram_list = n_gram_list(x, 2)
    frequency_Count, n_gram_probability_mean, n_gram_individual_probability = n_gram_probability_calculation(2, gram_list)
    print(f"{frequency_Count}, {n_gram_individual_probability}, {n_gram_probability_mean}\n")
    frequency_Count.clear()
    n_gram_probability_mean = 0
    gram_list.clear()
