# 8-9. Messages: Make a list containing a series of short text messages. Pass the  list to a function called show_messages(), which prints each text message. 

phrases = ['Hello',"What's up man?","You doing good!","Great work!"]

def show_messages(messages):
    """
    Prints each item in the list messages.
    """

    for message in messages:
        print(message)

show_messages(phrases)