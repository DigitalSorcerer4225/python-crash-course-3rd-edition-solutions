# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.  However, to avoid confusion, let’s call it a glossary. 
# •  Think of five programming words you’ve learned about in the previous  chapters. Use these words as the keys in your glossary, and store their  meanings as values. 
# •  Print each word and its meaning as neatly formatted output. You might  print the word followed by a colon and then its meaning, or print the word  on one line and then print its meaning indented on a second line. Use the  newline character (\n) to insert a blank line between each word-meaning  pair in your output. 

glossary = {'for loops': 'For loops is a technique in programming where a specific code snippet is iterated x amount of times',
    'strings' : 'Strings are data that represent texts',
    'integers' : 'Integers are data that represent integer-value numbers.',
    'variables' : 'In programming, specifically in python, variables are a reference to a stored memory location',
    'lists' : 'A list is a collection of elements.',
    }
for word in glossary:
    print(f"{word.title()}:\n")
    print(f"\t{glossary[word]}\n")