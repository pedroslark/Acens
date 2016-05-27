with open('numbers.txt', 'r') as myfile:
    data = myfile.read().replace('\n', ' ')[:-1]

numbers = data.split()
numbers1 = []

for number in numbers:
    consecutive = False
    for i in range(len(number)-1):
        if number[i] == number[i+1]: consecutive = True
    if not consecutive: numbers1.append(number)

numbers2 = []
for number in numbers1:
    sum = 0
    for i in number: sum += int(i)
    if sum % 2 == 0: numbers2.append(number)

numbers3 = [number for number in numbers2 if number[0] is not number[-1:]]

print len(numbers3)

## gg easy :)
