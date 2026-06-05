# What are for loops in Python?
# What are the ways of looping through a list in real-world practice?
# What problems does for loop solve in real-world applications?
# What errors are associated with a for loop?
# What are edge cases in which for loops have a hard time doing its purpose?
# How are for loops related to the concept of scope in programming
# What is a logical error in programming?


# For loop that prints out each name in a list of magicians:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


# For loop that praises each magician for their tricks

for magician in magicians:
    print(f"Well done, {magician.title()}, that was a great trick!")
    print("I am looking forward for your next trick!\n")

print("Thank you, everyone. That was a great magic show!")