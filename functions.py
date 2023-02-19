def my_first_function():
    print('This is my first function.')

# my_first_function()

def add(a: int, b: int) -> int:
    '''
    This function adds two values.
    '''
    return a + b

# answer = add(2, 5)
# print(answer)

def args_add(*values):
    total = 0
    for v in values:
        total += v
    return total

# print(args_add(1, 2, 3, 4, 5))

def my_fun(**data):
    return f'You are {data["name"]}, you live in {data["city"]}.'

print(my_fun(name='Rajesh', city='Surat'))

