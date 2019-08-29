n=int(input("enter the number of elements"))
arr=[]
for i in range(0,n):
    v=int(input("number"))
    arr.append(v)
num=int(input("enter the number to be searched"))
if num in arr:
    print("yes",num," is present")
else:
    print("no",num,"is not present")
