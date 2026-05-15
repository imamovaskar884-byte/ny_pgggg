class Message:
    __slots__ = ('text', 'author')

    def __init__(self, text, author):
        self.text = text
        self.author = author

    def format_msg(self):
        return f"{self.author}: {self.text}"

msg = Message("Система работает стабильно.", "Системный администратор")
print(msg.format_msg())
