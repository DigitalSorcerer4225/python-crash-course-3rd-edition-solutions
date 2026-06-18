# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as  keys in your dictionary. Create a dictionary of information about each city and  include the country that the city is in, its approximate population, and one fact  about that city. The keys for each city’s dictionary should be something like  country, population, and fact. Print the name of each city and all of the infor­ mation you have stored about it. 

cities = {'Davao': {'country': 'philippines','land area': '2,443.61 sq. km', 'population': '1,848,947' },
          'Manila': {'country': 'philippines', 'land area': '38.55 sq. km', 'population':  '1,900,000'},
          'Cebu':  {'country': 'philippines', 'landa area': '315 sq. km', 'population': '965,332'},
          }

for city, info in cities.items():
    print(f"\nInformation about {city.title()} City:\n")

    for key, value in info.items():
        print(f"\t{key.title()}: {value.title()}")