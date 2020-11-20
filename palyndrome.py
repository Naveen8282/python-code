def IsPalyndrome(input1):
    txt = input1[::-1]
    if txt == input1:
        return "yes"
    else:
        return "no"

str1=str(input("enter the string: "))
print ("is the string %s Palyndrome? %s" % (str1,IsPalyndrome(str1)))