# largest & smallest no in a list

numbers=[-12,233,45,12,94]
largest = numbers[0]
smallest = numbers[0]

# Loop through the list
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)