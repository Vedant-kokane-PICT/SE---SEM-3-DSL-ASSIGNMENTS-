# Name - Vedant Kokane
# Roll no - 21415


class Sort_percentage:

    def __init__(self,n):
        self.n = n

    # Function for finding length
    def length(self, x):
        length = 0
        for i in x:
            length = length + 1
        return length

    # Function for taking input of percentages
    def input_percentage(self):
        n = self.n
        percentage = []
        for i in range(n):
            p = float(input("Please enter percentages - "))
            percentage.append(p)

        return percentage

    # Function for Insertion Sort
    def insertion_sort(self,arr):
        a = arr
        n = self.length(arr)
        for i in range(n):
            temp = a[i]
            j = i-1
            while(j>=0 and a[j] >temp):
                a[j+1] = a[j]
                j = j - 1
            a[j+1] = temp
        return a

    # Function for Shell sort
    def shell_sort(self,arr):
        a = arr
        n = self.length(arr)
        gap = n//2
        while(gap>=1):
            j = gap
            while(j<n):
                i = j-gap
                while(i>=0):
                    if(a[i+gap] > a[i]):
                        break
                    else:
                        temp = a[i+gap]   
                        a[i+gap] = a[i]
                        a[i] = temp
                    i = i - gap
                j = j+1
            gap = gap//2
        return a


n = int(input("Please enter the total no of students - "))
s = Sort_percentage(n)
choice = "y"
percentages = s.input_percentage()

while choice != "n":
    print("=" * 90)
    print("1. Use Insertion sort ")
    print("2. Use Shell sort  ")
    print("=" * 90)
    c = int(input("Please type the operation to be performed : "))

    if c==1:
        insertion = s.insertion_sort(percentages)
        print(insertion)
    elif c==2:
        shell = s.shell_sort(percentages)
        print(shell)
    else:
        print("You have entered wrong choice.")

    choice = input("Do you want to search another roll no or exit (y/n) : ")