first_names = []
last_names = []
counter = 0

first_names_output = "first_names.txt"
last_names_output = "last_names.txt"

with open ("names.txt", "r") as f:
    for line in f:
        name = line.split(" ")
        first_names.append(name[0])
        last_names.append(name[1])
        
with open (first_names_output, "r+") as f:
    for line in first_names:
        f.write(line + "\n")
    print(f"Added {len(first_names)} first names to {first_names_output}")
    
with open (last_names_output, "r+") as f:
    for line in last_names:
        f.write(line)
    print(f"Added {len(last_names)} last names to {last_names_output}")