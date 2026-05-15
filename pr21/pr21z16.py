class Temperature:
    __slots__ = ('value',)

    def __init__(self, value_celsius):
        self.value = value_celsius

    def to_fahrenheit(self):
        return (self.value * 9/5) + 32

t = Temperature(20)
print(f"{t.value}°C равняется {t.to_fahrenheit()}°F")
