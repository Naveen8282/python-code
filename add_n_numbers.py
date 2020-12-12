b=int(input("enter how many numbers you need to sum:"))
a=b+1
c=b-1
list1=[]
for i in range(1,a):
    list1.append(i)
print(list1)
""" d=list1 """
k=0
for j in range(0,b):
    k=k+list1[j]
print("The total sum of %d number is equal to %d " %(b,k))








  




