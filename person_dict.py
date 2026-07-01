def build_person(first_name, last_name, age=None):
    """Return a dictonary of information abotu a person"""
    person = {'first': first_name.lower(), 'last': last_name.lower()}
    if age:
        person['age'] = age
    return person

boxer = build_person('manny', 'pacman', '43')
print(boxer)

npc = build_person('Rosana', 'Leal')
print(npc)