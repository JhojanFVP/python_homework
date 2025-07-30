# log-decorator.py
import logging

# Logger setup (one-time)
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.info(f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def accepts_args(*args):
    return True

@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator

# Main test code
if __name__ == "__main__":
    say_hello()
    accepts_args(1, 2, 3)
    keyword_only(name="Jhojan", course="Python")
