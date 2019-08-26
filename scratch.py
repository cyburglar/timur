numbers = [2, 3, 5, 2, 7, 9, 5]
uniques = [] # почему написанно именно uniques?
for number in numbers: #почему написано имеено number, мы ведь не определили ни как именно слово number
    if number not in uniques:
        uniques.append(number)
print(uniques)


