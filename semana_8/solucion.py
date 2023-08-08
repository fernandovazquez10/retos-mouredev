from datetime import datetime

def get_pseudo_random_number(time: datetime = datetime.now(), numbers :list = []) -> int:
    index = 0
    if not numbers:
        for i in range(1, 101): 
            numbers.append(i)
    for digit in str(time):
        digit : str
        if digit.isdigit():
            index += int(digit)

    if index % 2 == 0:
        index += 13
        index *= len(str(time))
    else: 
        index -= len(str(time))
        index *= 13

    while index < 1 or index > len(numbers):
        if index < 0: 
            index *= -3.454
        elif index > 100:
            index /= 2.647
        index = index + index % 7.263
    index_list = str(index).split('.')
    if len(index_list) == 2:
        index = int(index_list[1][:2])
    else:
        index = int(index)
    return numbers[index]

pseudo_random_number = get_pseudo_random_number()
print(pseudo_random_number)
