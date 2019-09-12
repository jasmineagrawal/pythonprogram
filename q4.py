class student:
    

    def _init_(self):
        self.stud_id=None
        self.age=None
        self.marks=None

    def val_marks(self):
        if(self.marks<=100 and self.marks>=0):
            return True
        else:
            return False

    def val_age(self):
        if(self.age>20):
            return True
        else:
            return False

    def check_qual(self):
        if(self.val_age() and self.val_marks()):
            if(self.marks>65):
                return True
            else:
                return False
        else:
            return False

    def set_stud_id(self,s_id):
        self.stud_id=s_id
    def get_stud_id(self):
        return self.stud_id

    def set_age(self,a):
        self.age=a
    def get_age(self):
        return self.age

    def set_marks(self,m):
        self.marks=m
    def get_marks(self):
        return self.marks
s1=student()
s1.set_stud_id(1)
s1.set_age(21)
s1.set_marks(95)

if(s1.check_qual()):
    print("addmission granted")
    print("students details are: \n studentid:",s1.get_stud_id(),"\n age:",s1.get_age(),"\n marks:",s1.get_marks())
else:
    print("addmission denied")


        
        
