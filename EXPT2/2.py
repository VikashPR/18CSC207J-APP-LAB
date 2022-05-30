def rotation(str1,str2):
    size1 = len(str1)
    size2 = len(str2)
    temp = ''

    if size1!=size2:
        return False
    temp = str1 + str2
    if(temp.count(str2)>0):
        return True
    else:
        return False

str1 = input("Enter the 1st string : ")
str2 = input("Enter the 2nd string : ")

if rotation(str1,str2):
    print("Rotationally equal")
else:
    print("Rotationally unequal")