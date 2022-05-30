a=[]
n=int(input("Enter the no of elements : "))
for i in range (n):
    a.append(int(input()))
count=0
m=[]
for i in a:
    if i not in m:
        m.append(i)
        count=count+1
print("Unique value in the list : ",count)