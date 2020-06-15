#check if chaaacter is vowel
ch=input("enter the character")
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("charac is vowel")
elif(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
    print("charac is vowel")
else:
    print("character is consonant")
print("\n\n")

#to find the greatest of the three
a=int(input(" enter first number "))
b=int(input(" enter second number "))
c=int(input(" enter third number "))
if(a>b):
    if(a>c):
        print(str(a)+" is the largest")
    else:
        print(str(c)+" is the largest")# wrong way to do it as condition for c
elif(b>c):                             #couldnot be checked
    print(str(b)+" is the largest")
else:
    print(" all numbers are equal")

#to enter the number and get the day
day=int(input(" enter the digit"))
if(day==1):print("monday")
if(day==2):print("tuesday")
if(day==3):print("wednesday\t"*5)
        
        
    
