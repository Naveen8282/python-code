
#First 10 even multiples of 13
lst=[]
for i in range (1,11):
    a=13*i
    b=lst.append(a)
print(lst) 

for i in range(0,10):
    if lst[i]%2==0:
        print(lst[i],end=" ")





