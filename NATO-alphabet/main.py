import pandas as pd

# Creating the data frame from the csv file
nato_data_frame = pd.read_csv('nato_phonetic_alphabet.csv')

# Creating the nato_dict from the csv dataframe using dict comprehension
nato_dict = {row.letter: row.code for index, row in nato_data_frame.iterrows()}

# Capturing user input



# Creating the list that contains the nato values for each alphabet in user's input
while True:
    try:
        user_value = input("Enter a word: ").upper()
        nato_list = [nato_dict[letter] for letter in user_value]
    except KeyError:
        print("Sorry, only letters")
    else:
        print(nato_list)


# Printing the list that contains the nato values for the user's input.
