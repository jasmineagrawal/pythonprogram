import random
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen=random.randint(8,15)
p= "".join(random.sample(s,passlen))
print(p)
