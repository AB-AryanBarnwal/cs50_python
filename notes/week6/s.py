pokemon_list = []

with open("s.csv") as file:
    for line in file:
        pok, type = line.rstrip().split(",")
        pokemon={"pok": pok, "type": type}
        pokemon_list.append(pokemon)

for p in sorted(pokemon_list):
    print(f"{p['pok']} is in {p['type']}")
