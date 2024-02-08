

# Custom decorator function
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # print("Something is happening before the function is called.")
        
        # Change letters to uppercase
        args = tuple(arg.upper() if isinstance(arg, str) else arg for arg in args)
        kwargs = {key: value.upper() if isinstance(value, str) else value for key, value in kwargs.items()}

        result = func(*args, **kwargs)
        # print("Something is happening after the function is called.")
        return result
    return wrapper

# Custom decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        # print("Something is happening after the function is called.")
        return result
    return wrapper

# Applying the decorator to a function
@uppercase_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Calling the decorated function
say_hello("alice")
