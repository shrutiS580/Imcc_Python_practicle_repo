name = input("Enter your name: ")

for char in name:
    if char in "aeiouAEIOU":
        name = name.replace(char, "z")

print(name) 
