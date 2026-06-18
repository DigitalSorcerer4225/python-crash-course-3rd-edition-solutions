# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so  each person can have more than one favorite number. Then print each person’s  name along with their favorite numbers. 

favorite_numbers = {'dante': [777, 63, 54], 'mica': [62, 999, 231, 54],
    'alice': [14, 46, 456], 'benson': [99, 0], 'pinky': [3, 3.12], 'vince': 7
    }

for person, numbers in favorite_numbers.items():
    # if one number only
    #     print number
    # else list
    #     loop through the numbers
    if isinstance(numbers, int):
        print(f"{person.title()}'s favorite number is: {numbers}.")
    else:
        fav_numbers = ""
        for number in numbers:
            number = str(number)
            fav_numbers += f"{number}, "
        message = f"{person.title()}'s favorite numbers are: {fav_numbers}"
        # print(message[:-2])- deletes the last comma
        print(message.rstrip(', ')) # can also use this method; it is much more simpler
