def selection(marks):
    for i in range (len(marks)):
        min = i
        
        for j in range(i + 1, len(marks)):
            if marks[min] > marks[j]:
                min = j

        marks[i],marks[min] = marks[min],marks[i]

    print("Marks of students after performing selection sort: ")
    
    for i in range(len(marks)):
        print(marks[i])


def bubblesort(marks):
    n = len(marks)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if marks[j] > marks[j+1]:
                marks[j],marks[j+1] = marks[j+1],marks[j]

    print("Marks of student after performing bubble sort: ")
    
    for i in range(len(marks)):
        print(marks[i])

def top_five_marks(marks):
    print("Top five marks are: ")
    print(marks[-5:n])

marks = []
n = int(input("Enter the student count: "))
print("Enter marks for ",n," students(PRESS Enter after each student) ")

for i in range(0,n):
    ele = int(input())
    marks.append(ele)

print("The marks of ",n," students are: ")
print(marks)

flag = 1

while flag ==1:
    print("-*-*-*-*-*Menu-*-*-*-*-")
    print("1.Selection Sort")
    print("2.Bubble Sort")
    print("3.Exit")
    
    ch = int(input("Enter your choice: "))

    if ch == 1:
        selection(marks)
        a = input("Do you want to display top five scores: (yes or no) ")
        if a == 'yes':
            top_five_marks(marks)
        else:
            print("Thank You")
        flag = 1
    
    if ch == 2:
        bubblesort(marks)
        a = input("Do you want to display top five scores: (yes or no) ")
        if a == 'yes':
            top_five_marks(marks)
        else:
            print("Thank You")
        flag = 0

    if ch == 3:
        print("\nThank You")
        flag = 0
    else:
        print("Invalid choice")
        flag = 0
