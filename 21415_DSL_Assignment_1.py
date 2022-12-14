# Roll no - 21415
# Name - Vedant Kokane

# Getting total no of students
total_students = int(input("Please enter total number of students : "))
universal_set = []
for i in range(1,total_students+1):
    universal_set.append(i)

# Getting students who play cricket
cricket = []
cricket_students = int(input("Enter total number of students who play cricket : "))
for i in range(cricket_students):
    cricket_roll = int(input(("Enter roll no who play cricket : ")))
    if cricket_roll in range(1,total_students+1):
        if cricket_roll not in cricket:
            cricket.append(cricket_roll)
    elif cricket_roll not in range(1,total_students+1):
        print("Enter a new number")
        new_roll_cricket =  int(input(("Enter roll no who play cricket : ")))
        if new_roll_cricket in range(1, total_students + 1):
            if new_roll_cricket not in cricket:
                cricket.append(new_roll_cricket)

print("List of Roll no's who play cricket",cricket)

# Getting students who play badminton
badminton = []
badminton_students = int(input("Enter total number of students who play badminton : "))
for i in range(badminton_students):
    badminton_roll = int(input(("Enter roll no who play badminton : ")))
    if badminton_roll in range(1,total_students+1):
        if badminton_roll not in badminton:
            badminton.append(badminton_roll)
    elif badminton_roll not in range(1,badminton_roll+1):
        print("Enter a new number")
        new_roll_badminton = int(input(("Enter roll no who play badminton : ")))
        if new_roll_badminton in range(1, total_students + 1):
            if new_roll_badminton not in badminton:
                badminton.append(new_roll_badminton)


print("List of Roll no's who play badminton",badminton)

# Getting students who play Football
football = []
football_students = int(input("Enter total number of students who play football : "))
for i in range(football_students):
    football_roll = int(input(("Enter roll no who play football : ")))
    if football_roll in range(1,total_students+1):
        if football_roll not in football:
            football.append(football_roll)
    elif football_roll not in range(1,total_students+1):
        print("Enter a new number")
        new_roll_football = int(input(("Enter roll no who play football : ")))
        if new_roll_football in range(1, total_students + 1):
            if new_roll_football not in football:
                football.append(new_roll_football)


# Function for removing Duplicate
def duplicate(list_a):
    list_b = []
    for i in list_a:
        if i not in list_b:
            list_b.append(i)
    return list_b

# Function for union of 2 sets
def union_of_set(list_a,list_b):
    list_c = list_a.copy()
    for value in list_b:
        if value not in list_c:
            list_c.append(value)
    return list_c

# Function for intersecton of 2 sets
def intersection_of_set(list_a,list_b):
    list_c = []
    for value in list_a:
        if value in list_b:
            list_c.append(value)
    return list_c

# Function for difference of 2 sets
def deference_of_set(list_a,list_b):
    list_c = []
    for value in list_a:
        if value not in list_b:
            list_c.append(value)
    return list_c
# Function for symmetric difference of 2 sets
def symmetric_difference_of_set(list_a,list_b):
    list_c = deference_of_set(list_a,list_b)
    list_d = deference_of_set(list_b,list_a)
    list_e = union_of_set(list_c,list_d)
    return list_e

# Printing all lists for Menu
print("List of Roll no's who play cricket",cricket)
print("List of Roll no's who play badminton",badminton)
print("List of Roll no's who play football",football)


# Defining Menu function
def menu(choice):
    if choice == "1":
        choice_1 = intersection_of_set(cricket, badminton)
        print(choice_1)
    elif choice == "2":
        choice_2 = symmetric_difference_of_set(cricket, badminton)
        print(choice_2)
    elif choice == "3":
        list_c = union_of_set(badminton, cricket)
        choice_3 = deference_of_set(universal_set, list_c)
        choice_3 = duplicate(choice_3)
        print(choice_3)
        print(len(choice_3))
    elif choice == "4":
        list_c = intersection_of_set(cricket, badminton)
        choice_4 = deference_of_set(football, list_c)
        choice_4 = duplicate(choice_4)
        print(choice_4)
        print(len(choice_4))
    else:
        print("You have selected wrong choice")
c = "y"
while c !="n" :
    print("--" * 30)
    print(" 1. List of students who play both cricket and badminton")
    print(" 2. List of students who play ether cricket or badminton but not both")
    print(" 3. Number of students who play neither cricket nor badminton")
    print(" 4. Number of students who play cricket and football but not badminton")
    choice_of_user = input("Please enter your choice : ")
    # Calling Choice function
    print("")
    menu(choice_of_user)
    c = input("Please enter y/n to play or not : ")
