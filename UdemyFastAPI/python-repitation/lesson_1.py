"""
Напишите программу Python, которая может выполнять следующие действия: -
У вас есть $50 - Вы покупаете товар, который стоит 15 долларов, который имеет налог 3% - С помощью print() Распечатайте,
сколько денег у вас осталось, после покупки товара."""

cost = 50
prosent = 3 / 100
consumption = cost - (15 + prosent)
print(consumption)
# wey - 2
mony = 50
item = 15
tex = .03


"""
Присвоение строк. (Это может быть сложно, поэтому не стесняйтесь смотреть решение, чтобы мы могли сделать это вместе) 

- Спросите пользователя, сколько дней до его дня рождения 

- Использование функции print().. Печать приблизительного количества недель до дня рождения - 1 неделя = до 7 дней.

"""

day = int(input(' day = '))

result = round(day / 7)
print(f'{result} weeks for his birth day')


"""
- Создайте список из 5 животных под названием zoo 
- Удалить животное по 3-му индексу. 
- Добавить новое животное в конце списка 
- Удалить животное в начале списка. 
- Печать всех животных 
- Печать только первых 3 животных
"""

zoo = ['lion', 'zebra', 'elephant', 'hippopotamus' , 'crocodile']

print(zoo.pop(3))
print(zoo)
print(zoo.append('tiger'))
print(zoo)
print("pop",zoo.pop(0))
for i in zoo:
    print(i)
print(zoo)
print(zoo[0:3])


"""
- Создание переменной класса, содержащей целое число от 0 до 100 
- Код if, elif, else операторов для печати буквенной оценки переменной класса числа 
Классов:
 A = 90 - 100 
 B = 80 - 89 
 С = 70-79 
 D = 60 - 69 
 F = 0 - 59
"""

grade = 69

if grade >= 90:
    print('A')
elif grade >=80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >=60:
    print('D')
elif grade <= 50:
    print('F')

"""
Дано: my_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"] 

- Создайте цикл while, который печатает все элементы my_list переменной 3 раза. 

- При печати элементов используйте цикл for для печати элементов 

- Однако, если элемент цикла for равен понедельнику, продолжайте без печати

"""

my_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]


c = 0
while c < 3:
    c += 1
    print(c)
    print(my_list)
    for x in my_list:
        if x == "Понедельник":
            continue
        print(x)


"""
Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Создание цикла for для печати всех ключей и значений 

- Создание новой переменной vehicle2, которая является копией my_vehicle 

- Добавить новую клавишу 'vehicle2' к переменной vehicle2, которая равна 4
"""

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
for x in my_vehicle.items():
    print(x)

vehicle2 = my_vehicle.copy()
print(vehicle2)
vehicle2['vehicle2'] = 4
print(vehicle2)

"""
- Создать функцию, которая принимает 3 параметра (имя, фамилия, возраст)

 и возвращает словарь, основанный на этих значениях
"""

def return_dict(name , surname , age):
    d = {'name' : name ,
    'surname' : surname,
    'age' : age,
    }
    return d
print(return_dict('rasul' , 'abdi' , 19))