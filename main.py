import pandas as pd
from bi_gram_calculation import cleanupString_bi_gram, n_gram_list_bi_gram, n_gram_probability_calculation_bi_gram
from tri_gram_calculation import cleanupString_tri_gram, n_gram_list_tri_gram, n_gram_probability_calculation_tri_gram

# df = pd.read_csv("/Users/cvkrishnarao/Desktop/n_gram_document_1_copy.csv")
# list_n_gram = list(df["SET 4"])

# Multiple Sentences
# # Bi-gram calculation
# for n_gram in list_n_gram:
#     x = cleanupString_bi_gram(n_gram)
#     gram_list = n_gram_list_bi_gram(x, 2)
#     frequency_Count, n_gram_probability_mean, n_gram_individual_probability = n_gram_probability_calculation_bi_gram(2, gram_list)
#     print(f"{frequency_Count}, {n_gram_individual_probability}, {n_gram_probability_mean}\n")
#     frequency_Count.clear()
#     n_gram_probability_mean = 0
#     gram_list.clear()

# Multiple Sentences
# # Tri-gram calculation
# for n_gram in list_n_gram:
#     x = cleanupString_tri_gram(n_gram)
#     gram_list = n_gram_list_tri_gram(x, 3)
#     frequency_Count, n_gram_probability_mean, n_gram_individual_probability = n_gram_probability_calculation_tri_gram(3, gram_list)
#     print(f"{frequency_Count}, {n_gram_individual_probability}, {n_gram_probability_mean}\n")
#
#     if frequency_Count and n_gram_probability_mean is not None:
#         frequency_Count.clear()
#         n_gram_probability_mean = 0
#         gram_list.clear()

# Single Tri-gram sentence
# n_gram = "Smart bot helps clean."
# x = cleanupString_tri_gram(n_gram)
# gram_list = n_gram_list_tri_gram(x, 3)
# frequency_Count, n_gram_probability_mean, n_gram_individual_probability = n_gram_probability_calculation_tri_gram(3, gram_list)
# print(f"{frequency_Count}, {n_gram_individual_probability}, {n_gram_probability_mean}\n")

# Single bi-gram sentence
n_gram = "Tasty pie."
x = cleanupString_bi_gram(n_gram)
gram_list = n_gram_list_bi_gram(x, 2)
frequency_Count, n_gram_probability_mean, n_gram_individual_probability = n_gram_probability_calculation_bi_gram(2, gram_list)
print(f"{frequency_Count}, {n_gram_individual_probability}, {n_gram_probability_mean}\n")