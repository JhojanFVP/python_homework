import os
print("Running from:", os.getcwd())

# log-decorator.py
import logging
import os

print("Running from:", os.getcwd())

logger = logging.getLogger("my_parameter_log")
logger.setLevel(logging.INFO)

log_path = os.path.join(os.path.dirname(__file__), "decorator.log")
logger.addHandler(logging.FileHandler(log_path, "a"))

# OPTIONAL: Also log to terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Logging:", func.__name__)  # TEMP DEBUG
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.info(f"return: {result}")
        for handler in logger.handlers:
            handler.flush()
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

if __name__ == "__main__":
    say_hello()
    accepts_args(1, 2, 3)
    keyword_only(name="Jhojan", course="Python")


