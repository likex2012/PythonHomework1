 #
# my_age = 12 #возраст
# print(my_age)
#
# # целые числа - integer - int
# res = 78/2
# print(5 + 7 - 8 * 12)
# print(res)
# print(2**3)
# print(4**3)
# print(7 // 2)  #целочисленное деление
# print(7 % 2)   # остаток от деления
# sec = 987
# print(sec // 60 // 60) # узнать количество часов
#
# # десятичные числа - float
# temp = 26.8
# temp = 9
# print(type(temp))  #тип переменной
#
# # строки - string -str
# name = 'Maria'
# name2 = 'Daria'
# print(name, name2)
# age = '67'
# symb = 'Hello how are you'
# print(name + name2) #арифметические действия со строками
# print(name * 5) #можно умножить строку на число- продублируется количество раз
# print(type(name))

# input ()
# age = input('Enter age: ')
# name = input('Enter name: ')
# print('Age:', age)
# print('Name:', name)

# n1 = input('n1: ')
# n2 = input('n2: ')
# print(type(n1))
# n1 = float(n1)
# n2 = int(n2)
# print(type(n1))
# print(n1 + n2)
#
# num = 123
# print(type(num))
# num = str(num)
# print(type(num))

# print(6 <= 8)
# print(7 == 8) #сравнение равно
# print(7 != 8) #сравнение не равно

# age = 97
# doc = input('есть ли права?')
# if age >= 18 and age < 100 or doc == 'yes':                        # двоеточие! скобки не нужны; and- дополнительное условие; or- или
#     print('можете ехать!')                          #не забывай кавычки!
#     print('удачного дня')
# else:
#     print('сначала получите права')

# color = 'brown'
# if color == 'red':
#     print('red')
# elif color == 'green':
#     print('green')
# elif color == "blue": # иначе если
#     print('blue')
# else:
#     print('такого цвета нет')


# while - условный цик
# count = 0
# while True:
#     print('hello')
#     age = int(input('age: '))
#     if age > 18:
#         count = count + 1                       #count += 1
#         if count > 3:
#             break

# n = 16543
# i = 0
# while n > 0:
#     last = n % 10 # 123/10= 12.3
#     i + 1           # i += 1
#     print('Сейчас цифр', i)
#     n = n // 10     # n//= 10
#     print(i, 'цифр в числе')

age = 8
name = 'nick'
city = 'spb'
print('my name is', age, 'my age is', name, 'i live in', city)
print(f'my age is {age}. My name is {name}. I live in {city}')