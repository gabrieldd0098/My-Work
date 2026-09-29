import pandas

# student_dict = {
#     "student": ["Holly", "Marc", "Spence", "Soho", "Rob", "Horace"],
#     "score": [56, 76, 98, 79, 61, 99]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.
#improved with TEE(F) ERROR handling
def gen_phon():
    word = input("Kindly Enter a WORD:\n").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("SORRY! Only letters allowed. No numbers, please!")
        gen_phon()
    else:
        print(output_list)

gen_phon()
