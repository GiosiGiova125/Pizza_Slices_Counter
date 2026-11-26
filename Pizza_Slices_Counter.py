school_friends = []
school_friends.append("Luca")
school_friends.append("Mario")
school_friends.append("Micheal")

sport_friends = []
sport_friends.append("Anna")
sport_friends.append("Lorenzo")

total_invites = sport_friends + school_friends

for x in total_invites:
    print(x)

tickets = ("VIP TICKET", " ") * 5
print(tickets)

pizzas = 3
pizza_slices = 8
total_slices = pizzas * pizza_slices

leftover_slices = total_slices % 5

if leftover_slices == 0:
    print("no slices left")
else:
    print("there is still some pizza")
