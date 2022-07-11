import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabets = {y.letter: y.code for (x, y) in data.iterrows()}
user_word = input("Enter a word:- ").upper()
user_code = [nato_alphabets[character] for character in user_word]
print(user_code)
