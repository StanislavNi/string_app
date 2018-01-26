# coding: utf8
# Script for working with the user's text
from handlers import InputHandlers, HandlerException



def text_info(text):
    # Count the length of the text
    print('Длина строки равна: ', len(text))
    string_list = text.split()
    # Count the number of letters
    print('Количество слов в тексте равно: ', len(string_list))
    # Count the number of numerals
    num = ([int(i) for i in string_list if i.isdigit()])
    print('Количество чисел в тексте равно: ', len(num))

    # Divide the text by strings with the length 25 symbols
    def max_string(s, n):
        """
        Divide 's'(user's text)
        by 'n'(string length)
        """
        return [text[i:i + n] for i in range(0, len(text), n)]
    print('Вывод текста по 25 символов: ',)
    for s in max_string(text, 25):
        print(s)

    def reverse(text):
        """
        Reverse user's text
        from the last symbol
        to the first
        """
        return text[::-1]

    reversed_text = reverse(text)
    # Print reversed strings with the length 25 symbols
    print('Вывод текста по 25 символов с конца: ')
    divided_reversed = (
        [reversed_text[i:i + 25] for i in range(0, len(reversed_text), 25)])
    for a in divided_reversed:
        print(a)


#TODO final handlers,

user_raw_input = input('Введите команду, строку, путь к файлу или URL: ')
try:
    text = InputHandlers().parse(user_raw_input)
except HandlerException as e:
    print(e)
else:
    text_info(text)
