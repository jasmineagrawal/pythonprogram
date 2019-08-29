n=int(input("enter the number for divisors to be found"))
arr=[]
def divisor(input):
      for i in range(1,n+1):
          if (n%i==0):
              arr.append(i)
      return arr
print("list of divisor",divisor(n))
