import random

n = int(input("Enter the num: "))
lst = []
for i in range(n):
    x = random.randint(0, 100)
    if i % 2 == 0:
        lst.append(1)
    else:
        lst.append(x % 5)
print(lst)


if __name__ == "__main__":
    generate_list = [random.randint(0, 10) for _ in range(n)]
    lst = [1 if  i % 2 == 0 else i % 5 for i in generate_list]
    print(generate_list, lst)
