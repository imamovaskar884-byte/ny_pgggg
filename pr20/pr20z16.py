class CelsiusDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('celsius', 0)

    def __set__(self, instance, value):
        instance.__dict__['celsius'] = value
        # Автоматически обновляем фаренгейты
        instance.__dict__['fahrenheit'] = value * 9 / 5 + 32

class Temperature:
    celsius = CelsiusDescriptor()
    
    def __init__(self):
        self.celsius = 0
        
if __name__ == "__main__":
    temp = Temperature()
    temp.celsius = 100
    print(f"C: {temp.celsius}, F: {temp.fahrenheit}") # Вывод: C: 100, F: 212.0