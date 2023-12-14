class SingletonExample(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Example(metaclass=SingletonExample):
    def __init__(self):
        self.instance = 1


example_1 = Example()
example_2 = Example()

example_1.instance = 2
example_2.instance = 4

print(example_1.instance)
print(example_2.instance)