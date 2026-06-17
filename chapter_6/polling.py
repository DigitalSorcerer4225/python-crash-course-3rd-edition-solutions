# 6-6. Polling: Use the code in favorite_languages.py (page 96). 
# Make a list of people who should take the favorite languages poll. Include  some names that are already in the dictionary and some that are not. 
# Loop through the list of people who should take the poll. If they have  already taken the poll, print a message thanking them for responding.  If they have not yet taken the poll, print a message inviting them to take  the poll. 


favorite_languages ={
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    } 

voters = ['jen', 'sarah', 'edward', 'phil', 'janet', 'jim', 'edmund']


for person in voters:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for your response, we will inform"
        "you of the results as soon as every person have casted their vote!\n")
    else:
        print(f"{person.title()}, you have not yet voted."
        " Please do take the time to take the poll. Thank you\n")
    