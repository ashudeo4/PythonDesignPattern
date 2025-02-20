class PythonWaySingleton:
    _instance = None

    def __new__(cls):

        if not cls._instance: #Note Lazy instantiation
            cls._instance = super().__new__(cls)
        
        return cls._instance
    
s1 = PythonWaySingleton()
s2 = PythonWaySingleton()

print(s1 is s2)
