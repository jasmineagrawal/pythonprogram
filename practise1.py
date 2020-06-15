#to check if you are allowed to vote
age=int(input("enter your age: "))
if(age>18):
    print("you are eligible to vote")
else:
    print("you have to wait "+ str(18-age)+" years to vote")
print("\n\n")

#to find the largest amongst the two numbers
a=int(input("enter the first number"))
b=int(input("enter the decind number"))
if(a>b):
    print(str(a)+" is greater than "+str(b))
    print("so greater is ",a)
else:
    print(str(b)+" is greater than "+str(a))
print("\n\n")

#to chek if the number is even or odd
k=int(input("enter a number"))
if(k%2==0):
    print("given number is even")
else:
    print("given number is odd")
print("\n\n")

#to convert upper to lower
ch=input("enter an alpabetic digit")
if(ch>='A'and ch<='Z'):
    print("given digit is in capital letter")
    ch=ch.lower()
    print(" in lower case it is ",ch)
else:
    ch=ch.upper()
    print(" given digit is small letter and its uppercase is ", ch)
print("\n\n")

#to check if the given year is leap year or not
yr=int(input("enter the year to check if its leap: "))
if(((yr%4==0) and (yr%100!=0)) or (yr%400==0)):
    print("given year is a leap year")
else:
    print("given number is not a leap year")
print("\n\n")

#to generate  salary bill
ch=input("enter the gender(m or f)")
sal=int(input("enter the salary of the employee"))
if(ch=='m'):
    bonus=0.05*sal
else:
    bonus=0.1*sal
subtotal=sal+bonus
print("total salary ="+str(sal))
print("after bonus ="+str(subtotal))
print("******************************")
if(sal<10000):
    extra_bonus=0.02*sal
    total=subtotal+extra_bonus
    print("extra bonus ="+str(extra_bonus))
    print("amount to be paid  :" ,total)
else:
    print("amount to be paid :",subtotal)
    
