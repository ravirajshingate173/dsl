def longestLength():

    str1 = input("Enter the string: ")
    list1 = str1.split()
    m = 0
    word = 0

    for i in range(len(list1)):
        len(list1[i])
        if m < len(list1[i]):
            m = len(list1[i])
            word = i
    print(list1)
    print("a) Longest word in above string is: ", list1[word])

def frequency():
    str1 = input("Enter the string: ")
    char = input("Enter the character: ")
    print(str1)

    counter = 0

    for i in range(len(str1)):
        if(char == str1[i]):
            counter+=1
    print("Character %s is present %i times in string %s"%(char,counter,str1))


def pallindrome():
    str2 = input("Enter the string to check is it pallindrome or not: ")
    str3 = str2[-1::-1]

    if(str2 == str3):
        print ("Above string is a pallindrome")
    else:
        print("Above string is not pallindrome")

def index():
    str1 = input("Enter the string: ")
    sub1 = input("Enter the substring: ")
    sublen = len(sub1)
    index1 = 0
    j = 0

    for i in range(len(str1)):
        if(sub1[j] == str1[i]):
            j = j + 1
            if(j == sublen):
                index1 = i - (sublen - 1)
                break
        else:
            j = 0

    print("Substring index: ",index1)

def occurence():
    str1 = input("Enter the string: ")
    str1 = str1.split()
    list2 = []

    for i in str1:
        if i not in list2:
            list2.append(i)

    for i in range(0, len(list2)):
        print("\nCount of frequency of", list2[i], " is: ",str1.count(list2[i]))


longestLength()
print()

frequency()
print()

pallindrome()
print()

index()
print()

occurence()
print()