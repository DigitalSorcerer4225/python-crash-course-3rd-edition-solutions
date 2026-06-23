# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the  number is a multiple of 10 or not. 

message = "Give me a number and I'll see if it is a multiple of 10 \n"
message += "Number: "
number = input(message)
number = int(number)

if number % 10 == 0:
    print("Your number is a multiple of ten!")
else:
    print("Your number is not a multiple of ten!")