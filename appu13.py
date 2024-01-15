#this is a code for understanding decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function called")
        func()
        print("Something is happening after the function called")

    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
