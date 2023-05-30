PLACEHOLDER =  '[name]'
with open(".\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_list = letter_file.read()
with open(".\\Input\\Names\\invited_names.txt") as names_file:
    names_list = names_file.readlines()
    for name in names_list:
        stripped_names = name.strip()
        final_letter = letter_list.replace(PLACEHOLDER, stripped_names)
        # print(final_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as ready_letter:
            ready_letter.write(final_letter)
