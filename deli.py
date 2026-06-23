# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various  sandwiches. Then make an empty list called finished_sandwiches. Loop through  the list of sandwich orders and print a message for each order, such as I made  your tuna sandwich. As each sandwich is made, move it to the list of finished  sandwiches. After all the sandwiches have been made, print a message listing  each sandwich that was made. 

sandwich_orders = ['salami', 'chicken tuna', 'hotdog', 'garlic', 'pepperoni']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Preparing your {sandwich} sandwich.")
    
    finished_sandwiches.append(sandwich)
    print(f"Your {sandwich} is ready!\n")


print("\n--- Today's Orders ---")

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} Sandwich")

# print(sandwich_orders)
# print(finished_sandwiches)

    