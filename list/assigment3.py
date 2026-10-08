# insert a item at 6th position this numbet must be 1/3rd of number stored at 4th position 
numbers = [2, 3, 4, 8, 6, 7, 8, 9]

numbers.insert(6, numbers[4] / 3)

print(numbers)