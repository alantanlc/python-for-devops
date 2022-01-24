import time

# Python decorators are a special syntax for functions which take other functions as arguments. Python functions are objects, so any function can take a function as an argument. The decorator syntax provides a clean and easy way to do this. The basic format of a decorator is:
def some_decorator(wrapped_function):
  def wrapper():
    print('Do something before calling wrapped function')
    wrapped_function()
    print('Do something after calling wrapped function')
  return wrapper
  
def timer(wrapped_function):
  def wrapper():
    start = time.time()
    wrapped_function()
    end = time.time()
    print(f'{wrapped_function.__name__} took {end - start} seconds to run')
  return wrapper
  
# You can define a function and pass it as an argument to this function:
def foobat():
  print('foobat')
  
f = some_decorator(foobat)

# f()

# The decorator syntax simplifies this by indicating which function should be wrapped by decorating it with @decorator_name. Here is an example using the decorator syntax with our some_decorator function:

@timer
def batfoo():
  print('batfoo')
  
batfoo()
