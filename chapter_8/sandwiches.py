# 8-12. Sandwiches: Write a function that accepts a list of items a person wants  on a sandwich. The function should have one parameter that collects as many  items as the function call provides, and it should print a summary of the sand­ wich that’s being ordered. Call the function three times, using a different num­ ber of arguments each time. 

def create_sandwich(*toppings):
    """
    Create a sandwich with as many toppings
    as the customer likes.
    """
    print(f"Making a sandwich with the following toppings:")

    for topping in toppings:
        print(f"\t- {topping.title()}")
    
    print(f"\nYour sandwich is done!\n")

create_sandwich('batteries','tires','water')
create_sandwich('cheese','ham','fish')
create_sandwich('peanut butter')