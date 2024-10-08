#author__uy_thea
#date__october_3_2024
#section_bscpe_2-2


list_num_one = [] #create a list1
list_num_two = [] #create a list2

#get all the values of list 1 
print("List Number 1")
while True:
    try:
        list_one = input("Enter double space to exit \nEnter anything: ")
        if list_one == "  ":
            break
    except:
        break
    else:
        list_num_one.append(list_one)

#get all the values of list 2
print("List Number 2")
while True:
    try:
        list_two = input("Enter double space to exit \nEnter anything: ")
        if list_two == "  ":
            break
    except:
        break
    else:
        list_num_two.append(list_two)


list_of_tuple = [(i,j) for i,j in zip(list_num_one,list_num_two)]

#print the result
print(list_of_tuple)

#end of the program 