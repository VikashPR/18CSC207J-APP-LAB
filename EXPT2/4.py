a=str(input("Enter the string : "))
pun='''!@#$%^&*()<>,.?/:;"'''
no_pun=""
for i in range (len(a)):
    if a[i] not in pun:
        no_pun=no_pun+a[i]

print(no_pun)