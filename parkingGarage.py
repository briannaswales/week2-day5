class Ticket():

<<<<<<< HEAD
    parking_tickets = []
    paid_tickets = []
    my_ticket = []

    def __init__(self, id):
        self.count = 0
        self.id = id

    def take(self, number):
        new_value = Ticket.ticket.pop(0)
        Ticket.my_ticket.append(new_value)

    def pay(self, number):
        num = input("What's your ticket nubmer?")

    def leave(self, leave):
        num = input("What's your ticket number?")


num_tickets = 10

tickets = []
for num in range(1, num_tickets + 1):
    tickets.append(Ticket(num))


def sale():
    while True:

        t = input(
            "Would you like to take a ticket, pay for your ticket, or leave? ")

        if t.lower == 'take':
            x = ticket.pop(0)
            myticket.append(x)

        elif t.lower == 'pay':
            num = input("What's your ticket number? ")

        elif num in myticket:
            paid.append(num)
            myticket.remove(num)
            print("You're all paid up!")

        elif t.lower == 'leave':
            num = input("What's your ticket number? ")

        elif num in paid:
            return ("Have a great drive!")

        else:
            print("Please pay for your ticket before you leave.")


sale()

# def __init__(self):
#     self.tickets = [x + 1 for x in range(10)]
#     self.current = {}

# def sell(self):
#     tickets = []
#     tickets.append(self.tickets.pop(0))
#     if self.tickets != None:
#         for i in range(len(tickets)):
#             self.current[tickets[i]] = 'Unpaid'
#         return f"Here's your ticket {tickets}"
#     else:
#         return "No more room in this lot."
#     sorted(self.tickets)

# def pay(self):
#     x = input("which ticket is yours? ")
#     self.current[x] = 'Paid'
#     return f"You're all paid up!"

# def leave(self, tickets):
#     self.tickets = tickets
#     self.tickets.append(self.tickets)
#     del self.current[self.tickets]
#     return "Have a great drive!"


class Test:

    def main():
        t.sell()
        print(t.tickets)
        print(t.current)

    def leave(self):
        pass
        self.tickets = input("What ticket are you returning? ")


td = Ticket(1)
td
# Test.main()
=======
    parking_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    paid_tickets = []
    my_ticket = []

    def take():
        if not Ticket.parking_tickets:
            print("No more spots left.")
        else:
            new_value = Ticket.parking_tickets.pop(0)
            Ticket.my_ticket.append(new_value)
            print(f"Here's your ticket! It's number {new_value}")

    def pay():
        num = int(input("What's your ticket nubmer?"))
        if num in Ticket.paid_tickets:
            print("You have already paid")
        else:
            Ticket.paid_tickets.append(num)
            Ticket.my_ticket.remove(num)
            print("You're all paid up!")

    def leave():
        num = int(input("What's your ticket number? "))
        if num in Ticket.paid_tickets:
            Ticket.paid_tickets.remove(num)
            Ticket.parking_tickets.append(num)
            print("Have a great drive!")
            
        else:
            print("Please pay for your ticket before you leave.")


def sale():
    
    
    while True:
        t = input("Would you like to take a ticket, pay for your ticket, or leave? ").lower()
        
        if t == 'take':
            Ticket.take()

        elif t == 'pay':
            Ticket.pay()
            
        elif t == 'leave':
            Ticket.leave()
            
        else:
            print("That's not a valid input.")
            
sale()
>>>>>>> ded64a666d14f2e33153f421d0623d32bd99d2c8
