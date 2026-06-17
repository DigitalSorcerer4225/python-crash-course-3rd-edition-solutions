# 6-5. Rivers: Make a dictionary containing three major rivers and the country  each river runs through. One key-value pair might be 'nile': 'egypt'. 

rivers = {'pulangi': 'bukidnon', 
          'hinatuan enchanted': 'surigao del sur',
          'agusan' : 'mindanao',
         }

for river, location in rivers.items():
    print(f"The {river.title()} runs through {location.title()}.")

print("Rivers included in the dictionary:")

for river in rivers:
    print(f"\t{river.title()}")

print("Countries included in the dictionary:")

for country in rivers.values():
    print(f"\t{country.title()}")