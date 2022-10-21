def selecting_action():
    selected = input("Plese select an action: (c/d) ")
    if selected == "c":
        coding_the_number()
    if selected == "d":
       ...

def coding_the_number():
    dictionary_positions = {}
    c_dictionary_positions = {}
    looking_for_number = 0
    search_start = 0
    number_found_at = ""
    added_0 = False
    code = input("Enter number you want to code: ")
    code_lenght = len(code)

    while len(dictionary_positions) != code_lenght:
        number_found_at = code.find(str(looking_for_number), search_start)
        if number_found_at != -1:
            search_start = number_found_at + 1
            dictionary_positions[number_found_at] = looking_for_number
        if number_found_at == -1:
            looking_for_number += 1
            search_start = 0

    code_lenght = len(code)
    if (code_lenght % 2) == 1:
        dictionary_positions[code_lenght] = 0
        code_lenght += 1
        added_0 = True

    #print("Dictionary before math " + str(dictionary_positions) + ",added 0: " + str(added_0) + ", lenght (with 0) = "+ str(code_lenght))
    position = 0
    code_lenght_copy = code_lenght + 1
    while code_lenght_copy != 1:
        answer = (dictionary_positions[position]**2+5)*code_lenght_copy+123
        c_dictionary_positions[position] = answer
        #print(answer)
        position += 1
        code_lenght_copy -= 1
    #print("Dictionary after math " + str(c_dictionary_positions))

    from_end = code_lenght - 1
    from_start = 0
    mixed_positions = ""
    while from_end > from_start:
        mixed_positions += str(c_dictionary_positions[from_end])+str(c_dictionary_positions[from_start])
        from_start += 1
        from_end -= 1
        
    print("You number has been coded to: " + mixed_positions  + "\nAgain?")
    again = input("(yes/no) ")
    if again == "yes":
            selecting_action()
    else:
            print("I hope I was usefull, Goodbye!")
            exit()

print("Welcome to 84´s (de)coder v 0.1")
selecting_action()
