# create a list of numbets and strings and set the values from users seprate the
#  list from the max numbersdisplay thr name in dicending 
data = []

n = int(input("How many values do you want to enter? "))

for i in range(n):
    value = input("Enter number or name: ")

    if value.isdigit():
        data.append(int(value))
    else:
        data.append(value)

numbers = []
names = []

for value in data:
    if isinstance(value, int):
        numbers.append(value)
    else:
        names.append(value)

numbers.sort(reverse=True)
names.sort(reverse=True)

print("Numbers in descending order:", numbers)
print("Names in descending order:", names)