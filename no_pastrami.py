# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure  the sandwich 'pastrami' appears in the list at least three times. Add code 
#  near the beginning of your program to print a message saying the deli has 
#  run out of pastrami, and then use a while loop to remove all occurrences of  'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
#  in finished_sandwiches. 

sandwich_orders = ['salami', 
                    'chicken tuna', 
                    'hotdog', 
                    'garlic', 
                    'pepperoni', 
                    'pastrami', 
                    'pastrami', 
                    'pastrami', 
                  ]
finished_sandwiches = []

print("We're sorry, the Deli has run out of Pastrami. Try out Today's Specials instead!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

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