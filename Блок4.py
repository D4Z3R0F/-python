#Блок 4

#Задание 1
a = "  Анна  "
b = a.strip()
print(b)

#Задание 2
a = "User_Name"
print(a.lower())

#Задание 3
a = "Я изучаю Java"
print(a.replace("Java", "Python"))

#Задание 4
a = "Капитанская дочка"
print(len(a))

#Задание 5
a = "Python"
b = a[0]
c = a[-1]
print(f"Первый символ: {b}")
print(f"последний символ: {c}")

#Задание 6
a = "PostgreSQL"
print(a[0:5])

#Задание 7
a = "Python"
print(a[::-1])

#Задание 8
a = "Python легко изучать"
b = a.split()
print(f"Количество слов: {b}")

#Задание 9
a = " А роза упала на лапу Азора "
clean = a.lower().strip()
b = clean == clean[::-1]
print(f"Палиндром: {b}")

#Задание 10
a = ' Анна '; ' USER@MAIL.RU '; ' идиот '
parts = a.split(";")
name = parts[0].strip(" ").capitalize()
email = parts[1].strip(" ").lower()
book = parts[2].strip(" ").capitalize()
print(f"Имя: {name}")
print(f"Email: {email}")
print(f"Книга: {book}")