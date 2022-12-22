# Name - Vedant Kokane
# Roll no - 21415
# Implementation of linear, sentinel, binary and fibonacci search

class Student:
    def __init__(self, n):
        self.n = n

    # Function for finding length
    def length(self, x):
        length = 0
        for i in x:
            length = length + 1
        return length

    # Function for finding duplicate
    def duplicate(self,list_a):
        list_b = []
        for i in list_a:
            if i not in list_b:
                list_b.append(i)
        return list_b

    # Function for taking input numbers
    def input_roll_nos(self):
        student = []
        for i in range(self.n):
            roll = int(input("Enter roll no's : "))
            if roll in range(1,self.n+1):
                if roll not in student:
                    student.append(roll)
        return student

    # Function for Linear search
    def linear_search(self,student,key):
        c = 0
        no = 0
        student = self.duplicate(student)
        n = self.length(student)
        print(student)
        for i in range(n):
            if student[i] == key:
                print("Roll no has attended the training program ")
                c = c+1
                no = i+1
        if c==0:
            print("The entered Roll no has not attended the training program. ")
        return no

    # Function for Sentinel search
    def sentinel_search(self,student,key):
        no = 0
        student = self.duplicate(student)
        length = self.length(student)
        last = student[length-1]
        student[length-1] = key
        i = 0

        while student[i] != key:
            i = i + 1
        student[length-1] = last
        if (i < length-1) or (key == student[length-1]):
            print("Roll no has attended the training program ")
            no = i+1
        else:
            print("The entered Roll no has not attended the training program. ")

        return no

    # Function for Binary search
    def binary_search(self, student, key):
        c = 0
        no = 0
        student = self.duplicate(student)
        student.sort()
        n = self.length(student)
        s = 0
        e = n - 1
        mid = 0
        while (s <= e):
            mid = (s + e) // 2
            if student[mid] == key:
                print("Roll no has attended the training program ")
                return mid
            elif student[mid] < key:
                s = mid + 1
            elif student[mid] > key:
                e = mid - 1

        return -1



    # Function for Fibonacci search
    def fibonacci_search(self,a,n,key):
        f = []
        first = 0
        second = 1
        f.append(first)
        f.append(second)
        for i in range(1,20+1):
            third = first + second
            f.append(third)
            first = second
            second = third
        k = 0
        while(f[k]<=key):
            k = k + 1
        if f[k]==0 :
            print("Not Present")
            return -1
        offset = -1
        check = False
        while (f[k]>1):
            i = min(offset+f[k-2],n-1)
            if key == a[i]:
                check = True
                print("Present")
                return i
            elif key > a[i]:
                k = k - 1
                offset = i
            elif key< a[i]:
                k = k - 2
        if check==False:
            print("Not Present")


n = int(input('Enter the total no of students in who attended the training program : '))
s = Student(n)
studuent_rollno = s.input_roll_nos()
print(studuent_rollno)
choice = "y"
while choice != "n":
    print("=" * 90)
    print("1. Use Linear search ")
    print("2. Use Sentinel search  ")
    print("3. Use Binary search  ")
    print("4. Use Fibonnaci search  ")
    print("=" * 90)
    c = int(input("Please type the operation to be performed : "))
    key = int(input("Enter roll no that to be searched : "))
    if c==1:
        s.linear_search(studuent_rollno, key)
    elif c==2:
        s.sentinel_search(studuent_rollno, key)
    elif c==3:
        s.binary_search(studuent_rollno, key)
    elif c==4:
        s.fibonacci_search(studuent_rollno,n,key)
    else:
        print("You have entered wrong choice.")

    choice = input("Do you want to search another roll no or exit (y/n) : ")
