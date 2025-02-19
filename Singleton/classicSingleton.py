class ClassicSingleton:
    _instance =  None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if not cls._instance: #Note : Lazy instantiation
            cls._instance = cls.__new__(cls)
        return cls._instance
    

# Two type of instantiation
# lazy and eager instantiation
