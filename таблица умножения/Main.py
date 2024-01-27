from colorama import Fore, Style, Back, init


# # # import requests




# # # init()

# # # # # # Урок 1

# # # # a=input("введите имя: ")
# # # # print(a)



# # # # Функции
# # # # print()
# # # # input()
# # # # type()
# # # # len()

# # # # Переменные
# # # # name = "Андрей"
# # # # age= 11
# # # # last_name = "Чернуха" #snake case
# # # # lastName = "Смышников" #camel case



# # # # Типы данных
# # # # Простые
# # # # a=17
# # # # b=17.3
# # # # c="minecraft"

# # # # Методы
# # # # Методы для строк
# # # # print(c.capitalize())
# # # print(c.upper())
# # # print(c.isdecimal())

# # # Проверка на Типы данных
# # # print(type(c))
# # # print(type(b))

# # # Проверка количества букв (символов) в слове
# # # a= "кот"
# # # print(len(a))


# # # # # Урок 2
# # # # # >, <, >=, <=, ==, !=
# # # # # print(10!=9)




# # # # # a=float(input("Введите число: "))
# # # # # b=float(input("Введите число: "))

# # # # # print(a+b)
# # # # # print(a!=b)
# # # # # print(a<=b)
# # # # # print(a>=b)
# # # # # print(a==b)

# # # # # print(type(a))

# # # # # Перевод типов данных
# # # # # Функции
# # # # # int()
# # # # # float()
# # # # # str()


# # # # # Control Flow, Управление потоком. Условия: if-else

# # # # # name=input('введите имя: ')
# # # # # if name == "Андрей":
# # # # #   print('привет,Андрей')
# # # # # elif name == "Егор":
# # # # #   print("блаблабла")
# # # # # else:
# # # # #   print('до свидания')

# # # # # a=float(input ("число:"))
# # # # # b=float(input ("число:"))
# # # # # c=a>b
# # # # # print("Первое число больше второго:")
# # # # # print(c)
# # # # # d=a==b
# # # # # print("Первое число равно второму:")
# # # # # print(d)

# # # # # if a>b:
# # # # #   print("A>B")
# # # # # else:
# # # # #   print("A<B")
# # # # # a=55
# # # # # b=44
# # # # # print(a>b)

# # # # # Урок 3. Цикл
# # # # # while
# # # # # for


# # # # day = 1
# # # # while day <= 1000 :
# # # #   print(f"{day} кирок ")
# # # #   day = day - 1000
  



# # # # Бесконечная Таблица умножения
# # # # Размер таблицы (10x10, 1000x1000)

# # # # Максимальное число
# # # # n=2
# # # # # Стартовый множитель
# # # # i=1

# while i<=n:
#   # Второй множитель
#   j=1
#   while j<=i:
#     result = i*j
#     print (f"{i} * {j} = {result}")
#     j=j+1
#   i=i+1




# # Ресторан PlaystationfoOd

# print("Привет, я ресторан PlaystationfoOd")
# print("Вот наше меню!")
# print("--------------")
# print("1.Стейк из говядины")
# print("2.Мохито классический(безалкогольный)")
# print("3.Картофель фри")

# print("0- ДЛЯ ЗАВЕРШЕНИЯ ЗАКАЗА")

# print("_____________________")

# order = []

# while True:
#   action=input("введите номер заказа: ")
  
#   if action == "0" :
#     break
#   elif action == "1" :
#     order.append("Стейк из говядины")
#     print('Стейк из говядины добавлен в корзину?')
#   elif action == "2" :
#     order.append("Мохито классический(безалкогольный)")
#     print('Мохито классический(безалкогольный) добавлен в корзину?')
#   elif action == "3" :
#     order.append("Картофель фри")
#     print('Картофель фри добавлен в корзину?')
#   else:
#     print("Такого блюда нет!")
  
# print(f"ваш заказ:{order}")
# print(f"№ Заказа: {random.randint(1,2000)} ")
# print(random.choice(["Камень", "Ножницы", "Бумага"]))

# random.seed(224142346142374)
# print(random.random())

# while True:
#   print(random.randint(1000,2000))

# Урок 4


# fruits=["Банан","яблоко","мандарины"]
# print(fruits)
# print(fruits[0])
# print(fruits.count("яблоко"))
# print(fruits.pop())
# print(fruits.pop())
# print(fruits)
# fruits.clear()
# fruits.append("Киви")
# fruits.append("Ананасы")
# fruits.append("Апельсины")

# fruits.sort()
# print(fruits.reverse())
# fruits.insert(1,"Яблоко")
# fruits.remove("Апельсины")

# print(type(fruits))


# name = "Имя"
# a = 1
# b = 10.5
# c = [""]



# Задание: Создание списка и применение методов

# 1. Создайте пустой список с именем my_list.

# 2. Добавьте в список пять целых чисел по вашему выбору.

# 3. Выведите содержимое списка на экран с помощью команды print().

# 4. Используя метод append(), добавьте в список ещё одно целое число.

# 5. Выведите обновленное содержимое списка на экран.

# 6. Используя метод insert(), вставьте целое число в середину списка.

# Как работает insert?
# my_list.insert(2, "яблоко")
# добавляется яблоко на позицию 2 в массиве

# 7. Снова выведите обновленное содержимое списка на экран.

# 8. Используя метод remove(), удалите один из элементов списка.

# 9. Выведите содержимое списка после удаления элемента.

# 10. Используя метод sort(), отсортируйте элементы списка в порядке возрастания.

# 11. Выведите отсортированный список на экран.

# 12. Используя метод reverse(), переверните порядок элементов списка.

# # # # 13. Выведите список в обратном порядке.
# # # # 14:56


# # # # fruits=["майнкрафт","роблокс","форза"]
# # # # print(fruits)
# # # # # print(fruits.append("текст"))

# # # # Урок 5


# # # # fruits= ("майнкрафт","роблокс","форза")
# # # # print(type(fruits))
# # # # fruits.index(1)

# # # # # Типы данных 

# # # # Простые типы данных
# # # # int() - integer 10
# # # # float() - дробные числа 10.5
# # # # str() - string "Строка с текстом"


# # # # list() - [] - изменяемый массив
# # # # tuple() - () - неизменяемый массив (кортеж)
# # # # dict() - {} - Словарь (объект)

# # # # dog = {
# # # #   "Name": "Бобик",
# # # #   "возраст": 1,
# # # #   "пол": "м",
# # # #   "команды": ["фас", "палка", "суслик"],
# # # #   "цвет": ("оранжевый","белый")
# # # # }


# # # # print(dog["Name"])
# # # # print(dog["возраст"])
# # # # print(dog["команды"][2])

# # # # for key in dog:
# # # #   print(key)
  
# # # # for value in dog.values():
# # # #   print(value)

# # # # for key, value in dog.items():
# # # #   print(f"{key} - {value}")

# # # # games = ["форза","GTA","nfs"]
# # # # for game in games:
# # # #   print(game)



# # # # ндрей. Задачка на ДЗ.

# # # # Придумать интересный объект (словарь) для проекта.

# # # # Наши основные действия в программе будет такие:

# # # # Вводится одно из возможных действий:
# # # # 1 — Показать,
# # # # 2 — Добавить,
# # # # 3 — Изменить,
# # # # 4 — Удалить,
# # # # 5 — Показать все имена в книге,
# # # # 6 — Показать все номера в книге.
# # # # 7 - Удалить все контакты
# # # # 8 - Выход

# # # # Пример объекта:

# # # # telephones = {
# # # # "Андрей" : "8 (800) 555-35-35",
# # # # "Соня" : "8 (752) 634-47-55",
# # # # "Рома" : "8 (568) 932-56-90"
# # # # }

# # # # movies = {
# # # # "Титаник": 1997,
# # # # "Звёздные войны": 1977,
# # # # "Форсаж 1": 2001,
# # # # }

# # # # Программа Телефонная книга

# # # # Вводится одно из возможных действий: 
# # # 1 — Показать, 
# # # 2 — Добавить, 
# # # 3 — Изменить, 
# # # 4 — Удалить, 
# # # 5 — Показать все имена в книге, 
# # # 6 — Показать все номера в книге.
# # # 7 - Удалить все контакты
# # # 8 - Выход

# def show_comands():
#   print(Fore.RED+Style.BRIGHT+"Телефонная книга")
#   print(Fore.BLUE+"1 — Показать")
#   print(Fore.CYAN+"2 — Добавить")
#   print(Fore.GREEN+"3 — Изменить")
#   print("4 — Удалить") 
#   print("5 — Показать все имена в книге")
#   print("6 — Показать все номера в книге")
#   print("7 - Удалить все контакты")
#   print("8 - Выход")
#   print("----------------------------------------")

# telefons = {
#   "Дедушка": 89271261424,
#   "Бабушка": 89271073212,
#   "Мама" : 89271481001,
# }

# def show_numbers(): 
#   for key, value in telefons.items():
#     print(f"{key} - {value}")
    
# def add_contact(): 
#   name = input("Введите имя: ")
#   number = int(input("Введите номер: "))
#   telefons[name] = number

#   print(Fore.LIGHTGREEN_EX+f"Контакт {name} добавлен")

# def edit_contact():
#   name=input("Введите имя для редактирования: ")
#   if name in telefons:
#       new_phone = int(input("Введите новый номер: "))
#       telefons[name] = new_phone   
#       print (Fore.LIGHTGREEN_EX+f"Контакт {name} изменен")
#   else:
#       print(Fore.LIGHTRED_EX+f"Контакт {name} не найден")

# def delete_contact():
#   name=input("Введите имя для удаления: ")
#   if name in telefons:
#       del telefons[name]
#       print (Fore.LIGHTGREEN_EX+f"Контакт {name} удален")

# def show_all_names():
#   for name in telefons:
#     print(name)

# def show_all_numbers():
#   for number in telefons.values():
#     print(number)
  
# def delete_all_contacts():
#   telefons.clear()
#   print(Fore.LIGHTGREEN_EX+"Все контакты удалены")
    
 

# while True:
#   show_comands()
#   action = input(Fore.WHITE+ "Введите действие: ")
#   if action == "1":
#     show_numbers()
#   elif action == "2":
#     add_contact()
#   elif action == "3":
#     edit_contact()
#   elif action == "4":
#     delete_contact()
#   elif action == "5":
#     show_all_names()
#   elif action == "6":
#     show_all_numbers()
#   elif action == "7":
#     delete_all_contacts()
#   elif action == "8":
#     break
#   else:
#     print(Fore.RED +"такой команды нет")


# Урок Функции


# 1
# def plus():

#   a=17
#   b=17
#   result= a+b
#   print(result)
  
# plus()

# 2
# def plus():

#   a=17
#   b=17
#   result= a+b
  
#   return result

# plus()
# print(plus())
# print(plus())

# a = "Андрей"
# print(a.upper())
# print(print("Hello"), print("Hello2"))

# 3
# def plus(a,b):
#   result= a+b
#   return result

# print(plus(17,17))
# print(plus(10,10))
# print(plus(1000, 100.5))


# 4
# def plus(a=10,b=34):
#   result= a+b
#   return result

# print(plus())

# 5
# def plus(a:int,b:float):
#   result= a+b
#   return result

# print(plus(10,11.45))

# 5
# def plus(a:list,b:list):
#   result= a+b
#   return result

# print(plus([1,2,3,4,5], [2,5,67,71]))

# Типы данных
#  str ("")
#  int,float 
#  list ([]) tuple (()) 
#  dict ({})

# def plus(a:int,b:int):
#   result= a+b
#   return result

# def minus(a:int,b:int):
#   result= a-b
#   return result

# def calc():
#   return plus(10,12), minus(20,10)
  
# print(calc())


# r = requests.get("https://www.google.com/папрвоылдлвоарп")
# print(r)
# print(r.content)





# ОШИБКИ - - - - - - - - - - -  
# 1. Синтаксическая ошибка
# while True:
  
# if 10 > 10;
#   print()

# 2. Матем ошибки. Ошибка деления на ноль ZeroDivisionError/Логическая ошибка

# print(10/0)


# 3. NameError Ошибка имени
# print(Int())
# print(Привет)

# 4. TypeError Ошибка типов

# a = 10
# b = 10
# print(a+b)

# c = [10, 50, 50, 10]
# d = {
#   "0": 10,
# }
# print(c+d)

# 5. IndexError Ошибка индекса

# c = [10, 50, 50, 10]
# print(c[3])


# 6. keyError Ошибка ключа

# d = {
#   "имя": ["Андрей", "Егор"]
# }
# print(d["имя"][2])


# 7. importError Ошибка импорта



import random

print()

