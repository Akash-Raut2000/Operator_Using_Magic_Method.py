class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

a = MyNumber(3)
b = MyNumber(5)
print((a + b).value)  # Output: 8
