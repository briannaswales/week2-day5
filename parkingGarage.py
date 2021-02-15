class Ticket:

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
