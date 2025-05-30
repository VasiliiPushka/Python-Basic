import random

def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) -1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False

nums = []
n = int(input('Сколько чисел в последовательности? '))
for _ in range(n):
    nums.append(random.randint(1, n))

new_nums = []
answer = []


for i_nums in range(0,len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Исходный список: ', nums)
print('Нужно чисел для полиндрома:', len(answer))
print('Список этих чисел:', answer)



#Для удобства возьмем сразу готовый список и для разных текстов просто будем его менять.
#Мы знаем, что нам каждый раз нужно будет брать элементы списка начиная с опреденного индекса
#А также нам нужно будет где-то хранить ответ
#для этого заведем еще 2 переменные new_nums[] и answer[]
#теперь нам нужен цикл для прохода по нашему списку
#дальше нам понадобиться каждый раз заполнять список из списка nums, причем начиная не с 0-го элемента, а с текущего
#   Так как это внутренний цикл, то его переменную назовем не i_elem, a j_elem

#После этого нам нужно проверить не является ли наш список полидромом
#Сделаем это с помощью вызова функции и передадим туда

# В функции мы могли бы использовать метод списков reverse, однако мы передаем в качестве аргумента список
#   в таком случае список изменится, здесь мы пойдем классическим путем через новую переменную и цикл


#Вернемся к основной программе
# если текущяя последовательность полиндром, то мы все уже нашли, нужно только записать в ответ те числа,
# которые стоят до того, в которых мы остановились в основном цикле
# также не забываем, что если последовательность не оказалась полидромом, то мы идем заново, а значит нужно переприсвоить новый список