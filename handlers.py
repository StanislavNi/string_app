import requests
from bs4 import BeautifulSoup


class HandlerException(Exception):
    pass

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
        try:
            r = requests.get(self.users_text, timeout=1)
        except requests.exceptions.RequestException:
            raise HandlerException('Сайта не существует')

        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            return ''.join(c for c in soup.text)
        else:
            raise HandlerException('Невозможно отобразить страницу')

    def is_valid(self, users_text):
        users_text = users_text.strip()
        if users_text.startswith('http'):
            self.users_text = users_text
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


class InputHandlers():
    input_handlers = [
        InputFileText(),
        InputUrlText(),
        ConsoleText(),
    ]

    def parse(self, user_input):
        text = None

        for editor in self.input_handlers:
            if editor.is_valid(user_input):
                text = editor.get_text()
                break

        return text