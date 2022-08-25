import math
import pandas as pd

n_gram_string_list = []
excel_2_gram_probabilities_list = []
excel_3_gram_probabilities_list = []
empty_2_gram_list = []
empty_3_gram_list = []
cleaned_input_string_list = []
probability_value_list = []

df_N_gram_2 = pd.read_csv("/Users/cvkrishnarao/Desktop/RA/n_gram_data_converted/n_gram_coca_x2w_utf_8.csv")
df_N_gram_3 = pd.read_csv("/Users/cvkrishnarao/Desktop/RA/n_gram_data_converted/n_gram_coca_x3w_utf_8.csv")


def cleanupString_tri_gram(uncleanedString):
    """
    :param uncleanedString: Uncleaned String with all special Characters and stuff
    :return: cleaned string with no special characters
    """
    uncleanedString = uncleanedString.replace('*', '')
    uncleanedString = uncleanedString.replace('(', '')
    uncleanedString = uncleanedString.replace(')', '')
    uncleanedString = uncleanedString.replace('-', '')
    uncleanedString = uncleanedString.replace(',', '')
    uncleanedString = uncleanedString.replace('.', '')
    uncleanedString = uncleanedString.replace(':', '')
    uncleanedString = uncleanedString.replace('?', '')
    uncleanedString = uncleanedString.replace('!', '')
    uncleanedString = uncleanedString.replace('\n', '')
    uncleanedString = uncleanedString.replace('\t', '')
    uncleanedString = uncleanedString.replace('-', '')
    w = uncleanedString.split()
    f = ""
    for wrd in w:
        wrd = wrd.lower()
        f = f + " " + wrd
    return f


def n_gram_list_tri_gram(input_Cleaned_string, n_gram_value):
    """
    :param input_Cleaned_string: Cleaned string without spaces or special characters
    :param n_gram_value: value of n-gram split == 2 or 3, 4, 5
    :return: Splitted work list according to the n_gram_values
    """
    split_string = input_Cleaned_string.split()
    if len(split_string) < n_gram_value:
        return
    else:
        for string in range(len(split_string)):
            y = split_string[string:string + n_gram_value]
            if len(y) == n_gram_value:
                n_gram_string_list.append(y)
        return n_gram_string_list


def n_gram_probability_calculation_tri_gram(n_gram_value, n_gram):
    """
    Calculates the respective score for the n-gram dataset. n_gram_value == 2 or 3, 4, 5
    n_gram = actual list of the splitted word count
    returns: excel_2_gram_probabilities_list with the frequency count for the values and the probability
    """
    if n_gram is not None:

        sum_frequencies = 0
        count_n_gram = len(n_gram)
        probability_value_list.clear()
        if n_gram_value == 3:
            excel_2_gram_probabilities_list.clear()
            for query_string in n_gram:

                # Getting the Single n-1 gram for 2 gram frequency
                query_string_search_one_gram = query_string[0:2]

                # Querying the result for 2-gram
                query_dataframe_2_gram = df_N_gram_2.loc[
                    (df_N_gram_2['Word_One'] == query_string_search_one_gram[0]) & (
                                df_N_gram_2['Word_Two'] == query_string_search_one_gram[1])]

                # Querying the result for 3-gram
                query_dataframe_3_gram = df_N_gram_3.loc[
                    (df_N_gram_3['Word_One'] == query_string[0]) & (df_N_gram_3['Word_Two'] == query_string[1]) & (
                                df_N_gram_3['Word_Three'] == query_string[2])]

                try:
                    # Getting values for 1 gram
                    values_frequency_two_gram = list(query_dataframe_2_gram["Frequency"])[0]
                except IndexError:
                    values_frequency_two_gram = 1

                try:
                    # Getting the values for 2 gram
                    values_frequency_three_gram = list(query_dataframe_3_gram["Frequency"])[0]
                except IndexError:
                    values_frequency_three_gram = 1

                if values_frequency_two_gram is None:
                    values_frequency_two_gram = 1

                if values_frequency_three_gram is None:
                    values_frequency_three_gram = 1

                # Dividing to get the values of the frequency
                divide = values_frequency_three_gram / values_frequency_two_gram

                # Probabilities
                probability_value = math.exp(math.log(divide))

                probability_value_list.append(probability_value)

                # calculation of the n_gram frequency
                sum_frequencies += sum_frequencies + math.exp(math.log(divide))
                excel_2_gram_probabilities_list.append(query_dataframe_3_gram.values.tolist())

                values_frequency_two_gram = int
                values_frequency_three_gram = int

            # Getting the Mean value of the n_gram
            mean_values = sum_frequencies / count_n_gram

            # Returning the list frequency and the mean values
            return excel_2_gram_probabilities_list, mean_values, probability_value_list

    else:
        return None, None, None
