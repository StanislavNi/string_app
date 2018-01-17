'''Пишем скрипт для работы с текстом пользователя'''
text = input ("Введите ваш текст ")

#Считаем длину строки в символах
print('Длина строки равна: ' + str(text.__len__()))

string_list = text.split()

#Считаем количество слов в тексте пользователя
print('Количество слов в тексте равно: ' + str(len(string_list)))

#Считаем количество чисел в тексте пользователя
num = ([int(i) for i in text if i.isdigit()])
print('Количество чисел в тексте равно: ' + str(num.__len__()))

#Возвращаем исходный код текста по строкам с максимальной длиной 25 символов
def max_string(s, n):
    return [ text[i:i+n] for i in range(0, len(text), n)]

print(max_string(text, 25))

#Возвращаем развернутые строки
def reverse(text):
    return text[::-1]
reversed_text = reverse(text)

#Выводим на экран развернутые строки по 25 символов
print([ reversed_text[i:i+25] for i in range(0, len(reversed_text), 25)])
