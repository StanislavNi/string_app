# coding: utf8
# Script for working with the user's text


class InputInterface(object):
    """
    Parent class
    """
    def get_text(self):
        raise NotImplementedError

    def is_valid(self, users_text):
        raise NotImplementedError


class InputFileText(InputInterface):
    """
    Get text from user's
    file
    """
    _filepath = None

    def get_text(self):
        f = open(self._filepath, 'r')
        return f.read()

    def is_valid(self, users_text):
        if users_text == 'text.txt':
            self._filepath = users_text
            return True
        return False


class InputUrlText(InputInterface):
    """
    Get text from user's
    URL
    """
    def get_text(self):
        return 'Яндекс.Поиск'

    def is_valid(self, users_text):
        users_text = users_text.strip()
        if users_text in ('https://ya.ru', 'ya.ru', 'http://ya.ru'):
            return True
        return False


class ConsoleText(InputInterface):
    """
    Get text from user's
    console
    """
    users_text = ''

    def get_text(self):
        return self.users_text

    def is_valid(self, users_text):
        self.users_text = users_text
        return True


user_raw_input = input('Введите команду, строку, путь к файлу или URL')


input_handlers = [
    InputFileText(),
    InputUrlText(),
    ConsoleText()
]

for editor in input_handlers:
    if editor.is_valid(user_raw_input):
        text = editor.get_text()
        break
    
    #else:
        #raise Exception('Невозможно обработать ввод')

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
    # TODO add description for user
    return [text[i:i+n] for i in range(0, len(text), n)]


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
divided_reversed = (
    [reversed_text[i:i+25] for i in range(0, len(reversed_text), 25)])
for a in divided_reversed:
    print(a)
