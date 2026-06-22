prompt = 'Tell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message.lower() != 'quit':
    message = input(prompt)
    
    # if message == 'quit':
    #     print("")
    # else:
    #     print(f"{message}\n")

    if message != 'quit':
        print(f"{message}\n")

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}!") 

