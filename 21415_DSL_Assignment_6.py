# Name - Vedant Kokane
# Roll no - 21415

class Sort_percentage:
    def __init__(self, n):
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
            p = float(input(f"Please enter percentage for {i+1} - "))
            percentage.append(p)

        return percentage

    # Function for Swaping
    def swap(self,a,b):
        temp = a
        a = b
        b = a
        return a,b

    # Function for making Partition
    def partition(self,a,low,high):
        pivot = a[low]
        start = low
        end = high
        while(start < end):
            while(a[start] <= pivot):
                start = start + 1
            while(a[end] > pivot):
                end = end - 1
            if(start < end):
                temp = a[start]
                a[start] = a[end]
                a[end] = temp
            
        temp = a[low]
        a[low] = a[end]
        a[end] = temp

        return end

    # Function for Quick Sort
    def quick_sort(self,array,low,high):
        if low < high:
            p = self.partition(array, low, high)
            self.quick_sort(array, low, p - 1)
            self.quick_sort(array, p + 1, high)

        return array


n = int(input("Please enter the total no of students - "))
s = Sort_percentage(n)

percentages = s.input_percentage()
print("The unsorted perectanges are -",percentages)
print("After performing Quick sort the sorted percentages are -",s.quick_sort(percentages,0,n-1))

