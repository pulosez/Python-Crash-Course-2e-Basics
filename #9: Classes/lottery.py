from random import choice


def set_player_tickets(tickets, num=4):
    player_list = []
    while len(player_list) < num:
        item = choice(tickets)
        if item not in player_list:
            player_list.append(item)
    print(f"Player tickets:\n{player_list}")
    return player_list


def get_winning_tickets(tickets):
    winning_list = []
    while len(winning_list) < 4:
        item = choice(tickets)
        if item not in winning_list:
            winning_list.append(item)
    print(f"\nWinning tickets:\n{winning_list}")
    return winning_list


def check_won(player_list, winning_list):
    print("Checking your ticket:")
    for ticket in player_list:
        if ticket in winning_list:
            print("Congratulations! You are win!")
            print(f"Your winning ticket: {ticket}")
            return True
    print("You didn't won!")
    return False


lottery_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']
player_tickets = set_player_tickets(lottery_tickets)

won = False
tries = 0

while not won:
    winning_tickets = get_winning_tickets(lottery_tickets)
    won = check_won(player_tickets, winning_tickets)
    tries += 1
print(f"Your tries: {tries}")
