numbers_list = [1, 2, 3, 4, 5, 6]
plus_one = []

for num in numbers_list:
    num += 1
    plus_one.append(num)

print(plus_one)

for i in range(len(numbers_list)):
    numbers_list[i] += 1

print(numbers_list)