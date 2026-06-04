# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who  would you invite? Make a list that includes at least three people you’d like to  invite to dinner. Then use your list to print a message to each person, inviting  them to dinner. 

guest = ['sal', 'samina', 'romel', 'tom hanks', 'forest gump', 'bones']
print(f"Would you like to come to my party, {guest[0].title()}?")
print(f"Would you like to come to my party, {guest[1].title()}?")
print(f"Would you like to come to my party, {guest[2].title()}?")
print(f"Would you like to come to my party, {guest[3].title()}?")
print(f"Would you like to come to my party, {guest[4].title()}?")
print(f"Would you like to come to my party, {guest[5].title()}?")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the  dinner, so you need to send out a new set of invitations. You’ll have to think of  someone else to invite. 
#  Start with your program from Exercise 3-4. 
# Add a print() call at the end of your program, stating the name of the guest who can’t make it. 
# Modify your list, replacing the name of the guest who can’t make it with the  name of the new person you are inviting. 
# Print a second set of invitation messages, one for each person who is still in  your list. 

canceled = guest.pop(1)
guest.insert(1, "Misha")
print(f"Would you like to come to my party, {guest[0].title()}?")
print(f"Would you like to come to my party, {guest[1].title()}?")
print(f"Would you like to come to my party, {guest[2].title()}?")
print(f"Would you like to come to my party, {guest[3].title()}?")
print(f"Would you like to come to my party, {guest[4].title()}?")
print(f"Would you like to come to my party, {guest[5].title()}?")
print(f"{canceled.title()} cannot make it.")

guest.insert(0, 'apple')
guest.insert(3, 'apa')
guest.append('luna')
print(f"Would you like to come to my party, {guest[0].title()}?")
print(f"Would you like to come to my party, {guest[1].title()}?")
print(f"Would you like to come to my party, {guest[2].title()}?")
print(f"Would you like to come to my party, {guest[3].title()}?")
print(f"Would you like to come to my party, {guest[4].title()}?")
print(f"Would you like to come to my party, {guest[5].title()}?")
print(f"Would you like to come to my party, {guest[6].title()}?")
print(f"Would you like to come to my party, {guest[7].title()}?")
print(f"Would you like to come to my party, {guest[8].title()}?")
print(f"\n\tNumber of people invited to dinner: {len(guest)}\n")
print("Friends and colleagues, I have found a larger table for us. We shall rejoice!")

print("It is with sadness and regret to inform you that the bigger table would not come in time for dinner and that I can only cater two guests. Rest assured, that we will have a bigger party next time and all will be invited!")

print(f"\n{guest.pop(0).title()}, I am sorry. I cannot cater you for dinner today. I'll call you next time.")
print(f"\n{guest.pop(2).title()}, I am sorry. I cannot cater you for dinner today. I'll call you next time.")
print(f"\n{guest.pop(2).title()}, I am sorry. I cannot cater you for dinner today. I'll call you next time.")
print(f"\n{guest.pop(2).title()}, I am sorry. I cannot cater you for dinner today. I'll call you next time.")
print(f"\n{guest.pop(2).title()}, I am sorry. I cannot cater you for dinner today. I'll call you next time.")
print(f"\n{guest.pop(2).title()}, I am sorry. I cannot cater you for dinner today. I'll call you next time.")
print(f"\n{guest.pop(2).title()}, I am sorry. I cannot cater you for dinner today. I'll call you next time.")
del guest[0]
del guest[0]
print(f"\n{guest}")
