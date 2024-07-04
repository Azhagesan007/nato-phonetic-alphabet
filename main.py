import pandas

data = pandas.read_csv("NATO.csv")

new_dict = {value.letter: value.code for (key, value) in data.iterrows()}

def words():
    word = input("Enter the word:\n")
    try:
        NATO_list = [new_dict[item.upper()] for item in word]
    except KeyError:
        print("Sorry, Only letters in alphabet is allowed")
        words()
    else:
        print(NATO_list)

words()

