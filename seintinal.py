def linear_search(a,n,c):
    for i in range(n):
        if c == a[i]:
            print(c, " is present at index ",i)
            break
    else:
         print("Student was absent in program")

def sentinel_search(a,n,c):
    last = a[n-1]
    a[n-1] = c
    i = 0

    while (a[i] != c):
        i += 1
        a[n-1] = last
        if ((i < n-1) or (a[n-1] == c)):
            print(c," is present at index",i)
            print("Student was present at program.")
            break

    else:
        print("Student was absent in program")

n = int(input("Enter the number of students: "))
a = []
print("Enter the roll no.: ")
for i in range(n):
    b = int(input())
    a.append(b)
print("List of students roll no. present in program: ")
print(a,"\n")

c = int(input("Enter the roll no. you want to search a student: "))
print("Select the searching method: ")

print("1.Linear search. \n2.Sentinel search.")

d = int(input())
if d == 1:
    linear_search(a,n,c)
else:
    sentinel_search(a,n,c)