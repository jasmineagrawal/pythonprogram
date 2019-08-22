arr=[]
lst=[]
n=int(input("enter the nummber of elements in the list"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
print("user defined list")
print(arr)
for i in arr:
    if i%2==0:
        lst.append(i)
print("new list")
print(lst)
