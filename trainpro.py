#list of train names
#need to import time
#list of passengers
#ticket generation
#type of tickets and ac,sleepers etc
#source and destination
import datetime
import random
class Train():
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats
#     We define the Train class, which takes in four parameter a train number, source, destination, and number of available seats. The __init__() method is called when a new Train object is created and initializes these attributes.

def display_info(self):
        print(f"Train number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available seats: {self.seats}")
        print()  # line break for each train information is displayed
        
          def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.seats -= num_tickets
            return pnr_list
        
 #    We define a book_tickets() method for the Train class, which takes a number of tickets as input and attempts to book that many tickets on the train. If there are enough available seats, the method generates a list of random PNRs equal to the number of tickets being booked, updates the number of available seats, and returns the list of PNRs. Otherwise, the method returns None to indicate that the booking failed.

