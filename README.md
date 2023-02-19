# Python tutorials
Hey friends, this is a repository for my [YouTube channel](https://www.youtube.com/channel/UCOT01XvBSj12xQsANtTeAcQ), you can learn about different aspects of Python here.

## Functions
Python functions are a piece of code that you can use over and over again without writing it. Like `print` is a function and we use it all the time, `range`, and all the other cool functions. You can write your own functions as all OOP language.

```
    def functionname():
        function body
```

Functions can have input arguments and return as well.

```
    def add(a: int, b: int) -> int:
        return a + b

    print(add(5, 7))
```

Functions can also have multiple input arguments with `*` sign. In the code below, the variable `values` will be passed as a `tuple` to the function `add`. 

```
    def add(*values):
        total = 0
        for v in values:
            total += v
        return total

    print(add(1, 2, 3, 4, 5, 6))
```

Functions can also have named arguments as well with `**` sign, In the code below, the variable `data` will be passed as a `dict` to the function `my_print`.

```
    def my_print(**data):
        return f'You are {data["name"]}'

    print(my_print(name='Rajesh'))
```

## Try except else finally
Python `try excpet` functionality is used to make sure your code works always.

* try -> try the piece of code
* except -> except anything wrong happen during the execuition
* else -> run if the execuition is success
* finally -> always run this part