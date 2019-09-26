class calldetails:
    def _init_(self):
        self.calling=""
        self.called=""
        self.duration=""
        self.Type=""

class Util:
    def _init_(self):
        self.list_of_call_objects=[]

    def parse_coustomer_list(self,list_of_call_string):
        for i in range(len(list_of_call_string)):
            lis=list_of_call_string[i].split(",")
            self.list_of_call_objects.append(lis)

    def to_print_call_details(self):
        for i in range(len(self.list_of_call_objects)):
              print(i)
              print("caling number:",self.list_of_call_objects[i][0],end="\n")
              print("called number:",self.list_of_call_objects[i][1],end="\n")
              print("caling duration:",self.list_of_call_objects[i][2],end="\n")
              print("caling type:",self.list_of_call_objects[i][3],end="\n")

call1='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call1,call2,call3]
u=Util()
u.parse_coustomer_list(list_of_call_string)
u.to_print_call_details()
