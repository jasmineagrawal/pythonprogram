str=input("enter the string")

def reverse(input):
    list=str.split(" ")
    list=list[-1::-1]
    str1=' '.join(list)
    return str1

print("output 1",reverse(str))
print("output 2",reverse(str)[::-1])

