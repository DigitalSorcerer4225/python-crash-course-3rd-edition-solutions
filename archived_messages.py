# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func­ tion send_messages() with a copy of the list of messages. After calling the func­ tion, print both of your lists to show that the original list has retained its messages. 

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

send_messages(unsent_list[:], sent_list)

print(unsent_list)
print(sent_list)