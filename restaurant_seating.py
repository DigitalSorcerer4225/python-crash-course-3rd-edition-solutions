# 7-2. Restaurant Seating: Write a program that asks the user how many people  are in their dinner group. If the answer is more than eight, print a message say­ ing they’ll have to wait for a table. Otherwise, report that their table is ready. 

table = input("How many companions do you have for this dinner? ")
table = int(table)

if table > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Certainly. Your table is now ready.")
