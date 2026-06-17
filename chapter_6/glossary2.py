# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean  up the code from Exercise 6-3 (page 99) by replacing your series of print()  calls with a loop that runs through the dictionary’s keys and values. 
# When  you’re sure that your loop works, add five more Python terms to your glossary.  When you run your program again, these new words and meanings should  automatically be included in the output. 

glossary = {'for loops': 'For loops is a technique in programming where a specific code snippet is iterated x amount of times',
    'strings' : 'Strings are data that represent texts',
    'integers' : 'Integers are data that represent integer-value numbers.',
    'variables' : 'In programming, specifically in python, variables are a reference to a stored memory location',
    'lists' : 'A list is a collection of elements.',
    'Python' : 'A programming language',
    'dictionary' : 'a collection of key-value pairs',
    'set': 'an ordered collection',
    'key': 'In key-value pairs, it is a label/reference used that points to a value',
    'value': 'In key-value pairs, it is the information associated to a key.',
    }

for word, meaning in glossary.items():
    print(f"{word.title()}:\n")
    print(f"\t{meaning}\n")