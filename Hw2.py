import datetime


class Ticket:
    items=[]

    def __init__(self,ticket_type,price):
        self.ticket_type=ticket_type
        self.price=price
        self.balance = 0

    def __repr__(self):
        return f"Ticket_type:{self.ticket_type} price:{self.price} "

class Ticket_single(Ticket):
    @classmethod
    def add_ticket(cls,price='for a trip'):
        ticket_type = input('Enter ticket type: ')
        # price=input('enter ticket price:')
        id = Ticket_single.generate_id(ticket_type)
        if id in Ticket.items:
            print("This Ticket is notavailabe , Your Ticket has expired")
        else:
            Ticket.items.append(id)
            return cls(ticket_type,price)

    @staticmethod
    def generate_id(str1):
        return f"{str1.lower()}"




# class Ticket_credit(Ticket):
#     @classmethod
#     def Totalinventory(cls,amount):
#         amount=int(input('enter amount'))
#         self.balance=self.balance+amount
#         print(f'mojodi is:{self.balance}')
        # self.balance.append(items)
        #     return cls(ticket_type,balance)






# class Ticket_credittime(Ticket,price,time):
#     pass
total=[]
total.append(Ticket('ticket_type','price'))

for i in range(2):
    temp_ticket=Ticket_single.add_ticket()
    if temp_ticket:
        total.append(temp_ticket)

print(total)

