#author__uy_thea
#date_October_3_2024
#section_bscpe2-2


value_list = [] #create a list for the all the values entered by the user

#this section will ask the user for integers
while True:
    try:
        value = int(input("Enter double space to exit \nEnter a value: "))
        value_list.append(value)
        if value == "  ":
            break
    except:
        break
        

square_odd_integers = [i**2 for i in value_list if i%2 != 0]
print(f"Original list = {value_list}")
print(f"Square odd integers = {square_odd_integers}")

#end of the program