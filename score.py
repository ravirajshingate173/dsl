def average(marks):
    sum = 0
    count = 0
    for i in range(len(marks)):
        if marks[i] != -999:
            sum += marks[i]
            count += 1  
    avg = sum / count
    print("Total marks: ", sum)
    print("Average marks: ", avg)

def Maxmarks(marks):
    for i in range(len(marks)):
        if marks[i] != -999:
            max = marks[0]
            break
    for i in range(1,len(marks)):
        if marks[i] > max:
            max = marks[i]
    return max

def Minmarks(marks):
    for i in range(len(marks)):
        if marks[i] != -999:
            min = marks[0]
            break
    for i in range(1,len(marks)):
        if marks[i] < min:
            min = marks[i]
            break
    return min

def Absentcount(marks):
    count = 0

    for i in range(len(marks)):
        if marks[i] == -999:
            count += 1
    return count

def maxFreq(marks):
    freq = {}
    for i in marks:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    return(max(freq,key=freq.get))


marks = []
n = int(input("Enter total number of students: "))
for i in range(n):
    m = int(input("Enter marks of student "+str(i+1)+" : "))
    marks.append(m)

flag = 1

while flag == 1:
    print("*********MENU*********")
    print("1.Average score of class")
    print("2.Highest and lowest score of class")
    print("3.Number of students absent for test")
    print("4.Marks with highest frequency")
    print("5.Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        average(marks)
        flag = 1

    elif ch == 2:
        print("Highest score in the class: ",Maxmarks(marks))
        print("Lowest score in class: ",Minmarks(marks))
        flag = 1

    elif ch == 3:
        print("Number of students absent for test are: ",Absentcount(marks))
        flag = 1

    elif ch == 4:
        print("Marks with highest frequency is: ",maxFreq(marks))

    elif ch == 5: 
        print("Thank You")
        break

    else:
        print("Invalid choice")
        break

