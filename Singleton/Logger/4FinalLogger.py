from abc import ABCMeta, abstractmethod
import logging
import threading

class SingletonMeta(metaclass=ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().call(*args, **kwargs)
            return cls._instances[cls]

class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass
    @abstractmethod
    def info(cls, message: str):
        pass
    @abstractmethod
    def warning(cls, message: str):
        pass
    @abstractmethod
    def error(cls, message: str):
        pass
    @abstractmethod
    def critical(cls, message: str):
        pass

class Logger(BaseLogger):
    
    def __init__(self):
        self.logger = logging.getLogger("my_logger")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("my_log_file.log")
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message: str):
        self.logger.debug(message)
    def info(self, message: str):
        self.logger.info(message)
    def warning(self, message: str):
        self.logger.warning(message)
    def error(self, message: str):
        self.logger.error(message)
    def critical(self, message: str):
        self.logger.critical(message)

logger = Logger()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")