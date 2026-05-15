class Timer:
    __slots__ = ('start', 'end')

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def difference(self):
        return abs(self.end - self.start)

time = Timer(12, 50)
print(f"Разница во времени: {time.difference()} минут/секунд")
