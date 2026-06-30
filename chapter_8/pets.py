def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') #positional argument style; order matters
describe_pet(pet_name='apple', animal_type='cat') #keyword arguments; order doesn't matter



