def sort(numbers):
    
    for i in range(1, len(numbers)):

        key = numbers[i]

        x = i-1
        while x >= 0 and key < numbers[x]:
            numbers[x+1] = numbers[x]
            x -= 1
        numbers[x+1] = key


numbers = [7, 3, 15, 9, 13]
sort(numbers)
print(*numbers)