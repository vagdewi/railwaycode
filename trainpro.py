#list of train names
#need to import time
#list of passengers
#ticket generation
#type of tickets and ac,sleepers etc
#source and destination
import datetime
import random
print (25*"--" ,"HAPPY_JOURNEY",25*"--")
print("wlecome to ticket booking")
list_of_trains={"chennai_express":'12345',"tirupathi_express":'45678',"eastgost":'9876',"venkatadri_express":"45321","janmabumi":'45678'} 
username=input("enter passenger name:")
print("yes,start your ticket process:")
#print(50*"  ","PNRNO",random.randint(11111,1000000)) 
class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")
#c=Passenger("p",12,'female','9023456679')
#c.display_info()
# print(5*"*","list of trains",5*"*")
for k,v in list_of_trains.items():
            print ("trainname",k,"trainnum:",v)
ticketrate={"chennai_express":'240',"tirupasthi_express":'500',"eastgost":'630',"venkatadri_express":"450","janmabumi":'480'}
print(5*"_","list of trains and prices",5*"_")
#for t,r in ticketrate.items():
    #print("select_train:",t,"ticketrates:",r)
tra=input("enter your required train:")
pas=int(input("enter number of passengers:"))
if tra in ticketrate:
    print("ticket_rate:",ticketrate[tra])
    print("totalprice:",int(ticketrate[tra])*pas)
user_date=int(input("enter your reservation date:"))
print("  ")
date=datetime.datetime(2023,6,user_date)
print("your reservation date:",date)
print("your ticket was  reserved:",datetime.datetime.now())
user_date=int(input("enter your reservation date:"))
seat=input("select_seattype:")
class Train():
    def __init__(self, train_num,select_seat, source, destination, seats,):
        self.train_num = train_num
        self.select_seat=select_seat
        self.source = source
        self.destination = destination
        self.seats = seats
    def display_info(self):
        print("Train number:",self.train_num)
        print("selectseat:",self.select_seat)
        print("Source:",self.source)
        print("Destination:",self.destination)
        print("Available seats:",self.seats)
        print()  # line break for each train information is displayed
tr=Train("12345","Ac","vjy","hyd",2)
tr.display_info()
#print(10*"*","yes, ticket is conform",10*"*")
print (25*"--" ,"HAPPY_JOURNEY",25*"--")
#print("wlecome to ticket booking")
#username=input("enter passenger name:")
print("yes,start your ticket process:")
c=Passenger("p",12,'female','9023456679')
c.display_info()
print(50*"  ","PNRNO",random.randint(11111,1000000))  
print(5*"*","list of trains",5*"*")
print(tra)
print(pas)
print(date)
print(10*"*","yes, ticket is conform",10*"*")

        



        
    

