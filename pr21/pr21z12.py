class User:
    __slots__ = ('login', 'password')

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
        print("Пароль успешно изменен!")

u = User("admin", "old_pass123")
u.change_password("new_secure_pass")
