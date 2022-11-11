print("Welcome to 84´s (de)coder v 1.2\nType 'c' for coding or 'd' for decoding")
def selecting_action():
    selected = input("Select an action: (c/d) ")
    if selected == "c":
        coding_the_number()
    if selected == "d":
       decoding_the_number()
    else:
        print("Invalid input")
        selecting_action()

def run_again():
    again = input("(yes/no) ")
    if again == "yes":
            selecting_action()
    else:
            print("I hope I was usefull, Goodbye!")
            exit()

def coding_the_number():
    dictionary_positions = {}
    c_dictionary_positions = {}
    looking_for_number = 0
    search_start = 0
    number_found_at = ""
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

    #print("Dictionary before math " + str(dictionary_positions) + ", lenght = "+ str(code_lenght))
    position = 0
    while code_lenght != 0:
        answer = (dictionary_positions[position]**2+5)*code_lenght+123
        c_dictionary_positions[position] = answer
        #print(answer)
        position += 1
        code_lenght -= 1
    #print("Dictionary after math " + str(c_dictionary_positions))

    from_end = len(code) - 1
    from_start = 0
    mixed_positions = ""
    while from_end >= from_start:
        mixed_positions += str(c_dictionary_positions[from_end])
        if from_start != from_end:
            mixed_positions += str(c_dictionary_positions[from_start])
        from_start += 1
        from_end -= 1
        
    print("You number has been coded to: " + "\u001b[33m" + mixed_positions + "\u001b[37m" + "\nAgain?")
    run_again()

def decoding_the_number():
    d_dictionary_positions = {}
    rp_dictionary_positions = {}
    position = 0
    start_n = 0
    end_n = 3

    decode = input("Enter number you want to decode: ")
    decode_lenght = int(len(decode) / 3)
    
    while len(d_dictionary_positions) != decode_lenght:
        d_dictionary_positions[position] = decode[start_n:end_n]
        position += 1
        start_n += 3
        end_n += 3
    #print("Unsorted numbers: " + str(d_dictionary_positions))
    
    from_end = int(decode_lenght) - 1
    from_start = 0
    position = 0
    while len(d_dictionary_positions) != len(rp_dictionary_positions):
        rp_dictionary_positions[from_end] = d_dictionary_positions[position]
        position += 1
        if len(d_dictionary_positions) != len(rp_dictionary_positions):
            rp_dictionary_positions[from_start] = d_dictionary_positions[position]
        position += 1
        from_end -= 1
        from_start += 1
    #print("Sorted numbers: " + str(rp_dictionary_positions))

    decoded = ""
    position = 0
    for math in range(decode_lenght):
        decoded_answer = int((((int(rp_dictionary_positions[position])-123)/decode_lenght)-5)**0.5)
        decode_lenght -=1
        position += 1
        decoded += str(decoded_answer)

    print("You number has been decoded to: " + "\u001b[33m" + str(decoded) + "\u001b[37m" + "\nAgain?")
    run_again()

selecting_action()
