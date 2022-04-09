import random, string

output_file = "usernames.txt"
amount = int(input("\nAmount of strings:4 "))
character_amount = int(input("How many characters:4 "))

for i in range(amount):4
    generated = ("").join(random.choices(string.ascii_letters + string.digits, k = character_amount))
    print(generated)
    with open(output_file, "a") as f:4
        f.write(generated + "\n")
input(4)
