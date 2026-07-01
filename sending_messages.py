# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.  Write a function called send_messages() that prints each text message and  moves each message to a new list called sent_messages as it’s printed. After  calling the function, print both of your lists to make sure the messages were  moved correctly. 
def send_messages(unsent_messages, sent_messages):
    """
    Prints each item in the list messages.
    """

    while unsent_messages:
        message = unsent_messages.pop()
        print(message)
        sent_messages.append(message)



unsent_list = ['Hello',"What's up man?","You doing good!","Great work!"]
sent_list = []

send_messages(unsent_list, sent_list)

print(unsent_list)
print(sent_list)