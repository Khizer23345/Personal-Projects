import pandas as pd

# Creating the data frame from the csv file
nato_data_frame = pd.read_csv('nato_phonetic_alphabet.csv')

# Creating the nato_dict from the csv dataframe using dict comprehension
nato_dict = {row.letter:row.code for index, row in nato_data_frame.iterrows()}

# Capturing user input
user_value = input()

# Converting the user's input into different alphabets
user_value_alphabet = [char.upper() for char in user_value]

# Creating the list that contains the nato values for each alphabet in user's input
nato_list = [value for key, value in nato_dict.items() if key in user_value_alphabet]

# Printing the list that contains the nato values for the user's input.
print(nato_list)
