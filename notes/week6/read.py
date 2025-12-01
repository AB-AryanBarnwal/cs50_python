# with open("names.txt", "r") as pokeball:
#     lines = pokeball.readlines()
# for l in lines:
#     print(f"I choose you, {l.rstrip()}!")

n = []
with open("names.txt", "r") as pokeball:
    for line in pokeball:
        n.append(line.rstrip())

for names in sorted(n, reverse=True):
    print(f"I choose you, {names}!")

# with open("names.txt", "r") as pokeball:
#      for line in sorted(pokeball):
#           print(f"I choose you, {line.rstrip()}!")