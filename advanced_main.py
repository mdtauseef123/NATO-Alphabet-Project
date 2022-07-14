import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabets = {y.letter: y.code for (x, y) in data.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word:- ").upper()
    print("Sorry only letters in the alphabet please.")
    try:
        user_code = [nato_alphabets[character] for character in user_word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        """
        This is a very smart way of repetition without using while/for loop this is called Recursion
        So when the user enters characters which is other than alphabet then it will raise an error message and then it
        will ask for the word.
        """
        generate_phonetic()
    else:
        print(user_code)


generate_phonetic()
