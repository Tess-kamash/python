a=[1,1,2,3,5,8,13,21,34,5,5,8,9]
number=int(input("Enter a number: "))
b=[]
for i in a:
    if i<number:
        b.append(i)
print(b)