class Ticket():

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
        t = input(
            "Would you like to take a ticket, pay for your ticket, or leave? ").lower()

        if t == 'take':
            Ticket.take()

        elif t == 'pay':
            Ticket.pay()

        elif t == 'leave':
            Ticket.leave()

        else:
            print("That's not a valid input.")


sale()
