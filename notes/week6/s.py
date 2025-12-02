import csv

pokemon_list = []

with open("s.csv") as file:
    r = csv.reader(file)
    for name, attack in r:
        pokemon_list.append({"Name": name, "Attack": attack})

for p in sorted(pokemon_list, key=lambda pokemon: pokemon["Name"]):
    print(f"{p['Name']}! {p['Attack']}!")