class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs): #Note Lazy instantiation
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]
    

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
