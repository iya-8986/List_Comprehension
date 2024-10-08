#author__uy_thea
#date_october_3_2024
#section_bscpe_2-2

def vowelsToUpper():
    phrase = [] #create a list 
    while True: #ask the user for input
        try:
            word = input("Enter double space to exit \nEnter anything: ")
            if word == "  ": 
                break
        except:
            break
        else:
            phrase.append(word)

    #list comprehension 
    translation = [word.translate(str.maketrans("aeiou", "AEIOU")) for word in phrase]
    return translation
print(vowelsToUpper())

#end of the program    
           