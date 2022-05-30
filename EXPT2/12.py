def palindrome(x):
    x=x.lower()
    for i in range(0,len(x)//2):
        if(x[i]!=x[len(x)-i-1]):
            flag = False
        else:
            flag = True
    if(flag):
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

str = input("Enter a string : ")
palindrome(str)