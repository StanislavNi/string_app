# Script for working with the user's text
text = input("Введите ваш текст ")

# Count the length of the text
print('Длина строки равна: ', len(text))

string_list = text.split()

# Count the number of letters
print('Количество слов в тексте равно: ', len(string_list))

# Count the number of numerals
num = ([int(i) for i in text if i.isdigit()])
print('Количество чисел в тексте равно: ', len(num))

# Divide the text by strings with the length 25 symbols
def max_string(s, n):
    """
    Divide 's'(user's text)
    by 'n'(string length)
    """
    return [text[i:i+n] for i in range(0, len(text), n)]

for s in max_string(text, 25):
    print(s, '\n')

# Reverse the text
def reverse(text):
    """
    Reverse user's text
    from the last symbol
    to the first
    """
    return text[::-1]
reversed_text = reverse(text)

# Print reversed strings with the length 25 symbols
divided_reversed = ([reversed_text[i:i+25] for i in range(0, len(reversed_text), 25)])
for a in divided_reversed:
    print(a, '\n')











