class WriteOnceDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None: return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if self.name in instance.__dict__:
            raise AttributeError(f"Атрибут {self.name} можно установить только один раз")
        instance.__dict__[self.name] = value

class System:
    config = WriteOnceDescriptor()

if __name__ == "__main__":
    sys = System()
    
    sys.config = "Начальные настройки"
    print(f"Успех! Настройки: {sys.config}")
    
    try:
        sys.config = "Новые настройки"
    except AttributeError as e:
        print(f"Ожидаемая ошибка поймана: {e}")