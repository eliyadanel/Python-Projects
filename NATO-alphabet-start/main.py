import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_d = {row.letter: row.code for (index, row) in data.iterrows()}

def gen_phonetic():
    user_input = input("Enter the word you want to spell\n").upper()
    index_num = 0
    try:
        letter_l = [nato_d[letter] for letter in user_input]

    except KeyError:
        print("Sorry. This program only does letters.")
        gen_phonetic()

    else:
        for letter in letter_l:
            print(f"{letter[0]} for {letter_l[index_num]}")
            index_num += 1


continue_loop = True

while continue_loop:
    gen_phonetic()
    ask_user = input("Would you like to try another word?(y/n) ")
    if ask_user == 'n':
        continue_loop = False
    else:
        pass

