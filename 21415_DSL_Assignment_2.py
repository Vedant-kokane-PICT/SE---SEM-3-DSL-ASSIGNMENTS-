# Name - Vedant Kokane
# Roll no - 21415

class String_Operation:

    # Function for finding length of a string
    def length(self,string_a):
        length = 0
        for i in string_a:
            length = length + 1
        return length

    # Function for spliting a string in list
    def split_string(self,string_a):
        list_a = []
        temp = ''
        for i in string_a:
            if i == " ":
                list_a.append(temp)
                temp = ''
            else:
                temp = temp + i
        if temp:
            list_a.append(temp)  # for last word
        return list_a

    # Function for finding length longest word  in string
    def longest_in_string(self,string_a):
        list_a = self.split_string(string_a)
        max_length = 0
        for i in range(len(list_a)):
            count = 0
            for j in list_a[i]:
                count = count + 1
            if count > max_length:
                max_length = count
        print(max_length)
        return max_length

    # Function for finding frequency of a character
    def character_frequency(self,string_a):
        count = 0
        string_a = string_a.lower()
        char = input("Enter character : ")
        for i in string_a:
            if i==char:
                count = count + 1
        print(count)

    # Function to check pallindrome
    def pallindrome(self,string_a):
        reverse_string = ''
        leng = self.length(string_a)
        string_a = string_a.lower()
        for i in reversed(range(leng)):
            reverse_string = reverse_string + string_a[i]

        if reverse_string == string_a:
            print("It is a pallindrome")
        else:
            print("Not a pallindrome")

    # Function for First Occurence of sub string
    def sub_string_occurence(self,string_a):
        sub = input("Please enter a sub-string : ")
        m = self.length(string_a)
        n = self.length(sub)
        string_a = string_a.lower()
        leng = m - n + 1
        if n > m:
            print("The length of sub string is greater then string.")
        else:
            for i in range(leng):
                for j in range(n):
                    if string_a[i+j] != sub[j]:
                        break
                if j+1 == n:
                    print(i)
                    break

    def occurrence_of_word(self,string_a):
        duplicate = []
        string_a = string_a.lower()
        list_a = self.split_string(string_a)
        l = self.length(list_a)
        for i in range(0,l):
            word = list_a[i]
            count = 0
            if word not in duplicate:
                duplicate.append(list_a[i])
                for j in list_a:
                    if word == j:
                        count = count + 1
                    else:
                        count = count + 0
                print(word,"-",count)


string = input("Enter a String : ")
x = String_Operation()
choice = "y"

while choice != "n":
    print("=" * 90)
    print("1. To display word with the longest length")
    print("2. To determines the frequency of occurrence of particular character in the string")
    print('3. To check whether given string is palindrome or not')
    print("4. To display index of first appearance of the substring")
    print("5. To count the occurrences of each word in a given string")
    print("=" * 90)
    c = int(input("Please type the operation to be performed : "))
    if c==1:
        x.longest_in_string(string)
    elif c==2:
        x.character_frequency(string)
    elif c==3:
        x.pallindrome(string)
    elif c==4:
        x.sub_string_occurence(string)
    elif c==5:
        x.occurrence_of_word(string)
    else:
        print("You have selected a wrong choice.")

    print("Do you want to try any other operation ? (y/n)")
    choice = input("")


