
for x in range (4):
    for y in range (3):
        print(f'({x}, {y})')
print('game over')


numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ('')
    for count in range(x_count):
        output += 'x'
    print(output)



names = ['bob', 'mosh', 'sarah', 'mary']
print(names[1:3])


numbers = [3, 6, 2, 8, 4, 10]
max = numbers[4]
for number in numbers:
    if number > max:
        max = number
print(max)



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)


numbers = [5, 2, 1, 7, 4, 7]
numbers.append(20)
print(numbers)
print(numbers.index(7))
print(7 in numbers)
numbers.pop()
print(numbers)
numbers.insert(0, 57)
print(numbers)
numbers.remove(4)
print(numbers)
numbers.clear()
print(numbers)


numbers = [1, 1, 4]
print(numbers.count(1))

numbers = [1, 7, 3, 4]
numbers.sort()

print(numbers)
numbers.reverse()

print(numbers)
numbers2 = numbers.copy()

numbers.append(9)
print(numbers2)


numbers = [2, 3, 5, 2, 7, 9, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


a = 6
b = 4
print(a//b)

