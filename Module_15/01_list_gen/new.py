def lists(number) -> list[int]:
    odd_numbers_list = []
    for i in range(number + 1):
        if i % 2 == 1:
            odd_numbers_list.append(i)
    return odd_numbers_list

if __name__ == '__main__':
    numbers = int(input('Enter number: '))
    print(lists(numbers))

