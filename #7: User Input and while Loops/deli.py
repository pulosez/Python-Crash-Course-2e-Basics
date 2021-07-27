# 7.8-9.
sandwich_orders = ['chicken', 'egg', 'pastorami', 'fish', 'pastorami', 'cheese',
                     'pastorami', 'ham']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastorami' in sandwich_orders:
    sandwich_orders.remove('pastorami')
    
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe folloving sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} sandwich.")
