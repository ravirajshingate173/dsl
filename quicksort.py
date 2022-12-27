def input_perc():
    perc = []
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        perc.append(float(input("Enter percentage of student {0} : ".format(i+1))))
    return perc

def print_perc(perc):
    for i in range(len(perc)):
        print(perc[i], sep = "\n")


def partition(perc, start, end):
    pivot = perc[start]
    lower_bond = start + 1
    upper_bond = end

    while True:
        while lower_bond <= upper_bond and perc[lower_bond] <= pivot:
            lower_bond += 1

        while lower_bond <= upper_bond and perc[upper_bond] >= pivot:
            upper_bond -= 1

        if lower_bond <= upper_bond:
            perc[lower_bond],perc[upper_bond] = perc[upper_bond],perc[lower_bond]

        else:
            break

    perc[start],perc[upper_bond] = perc[upper_bond],perc[start]
    return upper_bond


def quicksort(perc,start,end):
    while start < end:
        part = partition(perc,start,end)
        quicksort(perc,start,part-1)
        quicksort(perc,part+1,end)
        return perc 

def topfive(perc):
    print("Top Five percentages are: ")
    print(perc[-5:len(perc)])

unsorted_perc = []
sorted_perc = []

flag = 1
while flag == 1:
    print("******MENU******")
    print("1.Accept the percentage of students")
    print("2.Display the percentage of students")
    print("3.Display sorted percentage of students")
    print("4.Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1: 
        unsorted_perc = input_perc()

    elif ch == 2:
        print_perc(unsorted_perc)

    elif ch == 3:
        print("Percentage of students after performing quick sort is: ")
        sorted_perc = quicksort(unsorted_perc,0,len(unsorted_perc) - 1)
        print_perc(sorted_perc)
        a = input("Do you want to display top 5 percentages(yes or no): ")
        if a == 'yes':
            topfive(sorted_perc)

    elif ch == 4:
        print("Thank You")
        flag = 0
    else:
        print("Invalid choice")
