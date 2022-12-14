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
    def fibonacci_search(self, student, key):
        first = 0
        second = 1
        fibonaci = []
        fibonaci.append(first)
        fibonaci.append(second)
        for i in range(self.n):
            third = first + second
            fibonaci.append(third)
            first = second
            second = third
        n = self.n
        m = 0
        student.sort()
        while fibonaci[m] < n:
            m = m+1
        off_set = -1
        while fibonaci[m]>1:
            mid = min(off_set + fibonaci[m-2],n-1)
            if key > student[mid]:
                m = m-1
                off_set = mid
            elif key < student[mid]:
                m = m-2
            else:
                print("Roll no has attended the training program ")
                return mid+1

        if(key==student[n-1]):
            print("Roll no has attended the training program ")

        if not fibonaci[m-1] and student[off_set+1]==key:
            return off_set + 1
        return -1


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
        s.fibonacci_search(studuent_rollno, key)
    else:
        print("You have entered wrong choice.")

    choice = input("Do you want to search another roll no or exit (y/n) : ")
