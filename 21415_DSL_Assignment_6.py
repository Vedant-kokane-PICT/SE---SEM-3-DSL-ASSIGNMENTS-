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
    def partition(self,array,low,high):
        i = low
        j = high - 1
        pivot = array[high]
        while i < j:
            while i < high and array[i] < pivot:
                i = i + 1
            while j > low and array[j] >= pivot:
                j = j - 1
            if i < j:
                temp = array[i]
                array[i] = array[j]
                array[j] =  temp
        
        if array[i] > pivot:
            temp = array[i]
            array[i] = array[high]
            array[high] =  temp

        return i

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

