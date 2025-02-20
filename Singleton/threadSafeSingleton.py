import threading


#Simple Singleton

# class ThreadSafeSingletion:
#     _instance =  None
#     _lock = threading.Lock()

#     def __new__(cls):
#         with cls._lock:  
#             if not cls._instance: 
#                 cls._instance = super().__new__(cls)
#         return cls._instance

#Using Metaclass

class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=ThreadSafeSingletonMeta):
    pass

def get_singleton_instance():
    s = Singleton()
    print(s)

threads = []
for i in range(10):
    t =  threading.Thread(target=get_singleton_instance)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("All threads have finished")
