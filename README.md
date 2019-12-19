# Advent of Code 2019

Language: `Python3`

Testing:

`python3 day1pt1.py < day1/data.in > data.out`

`diff data.out day1/expected1.out`

Increments: Day 2, 5, 7, 9, 11 (related to day 3 and day 8)

### Python Notes

- functions
  - In Python, function is first-class citizen
  - \*args: tuple
  - \*\*kwargs: dict
- dictionary
  - for key, value in dict.items():
  - del dict[key], dict.pop(key)
- list
  - for idx, elem in enumerate(list)
  - sorted(list)
  - list comprehension: create new list
- set
  - set1.intersection(set2)
  - set1.difference(set2)
  - set1.symmetric_difference(set2)
  - set1.union(set2)
- numpy
  - np.array(list)
  - element-wise calculation, subsetting
- pandas
  - pd.DataFrame(dict)
  - pd.read_csv(file, index_col = 1)
  - df.index
  - Select columns:
    - Series: table[column];
    - DataFrame: table[[colum1, ...]]
  - Select rows:
    - table[start:end]
    - table.iloc[index]
    - table.loc[[[label1, ...]]
- generators
  - yield
- exception handling
  - try, except, raise
- re
  - ^: at the begining of a line
  - |: OR operator
  - (): group
  - \*: repeat 0 or more times
  - ?: un-greedy match
  - .: any non-newline character
  - re.comple(regex): pattern
  - re.search(pattern, string): Match
  - re.match(pattern, string): boolean
  - email pattern: r"\\"?([-a-zA-Z0-9.`?{}]+@\w+\\.\w+)\\"?"
- data serialization
  - json
    - json.loads(json_string)
    - json.dumps(object)
  - others: pickle
- functools
  - functools.partial(funct, args)
- code introspection
  - help()
  - dir()
  - hasattr()
  - id()
  - type()
  - repr()
  - callable()
  - issubclass()
  - isinstance()
  - \_\_doc\_\_
  - \_\_name\_\_
- Closure
  - Nested functions can access the variables of the enclosing scope. However, they are readonly.
  - Use `nonlocal` to modify them
  - A function can return another function
- Decorator
  - bottom up
  - @functools.wraps(func): preserve original function name and docstring
  - Can be used to change input, change output, do checking
  - datacamp.com/community/tutorials/decorators-python
  - https://wiki.python.org/moin/PythonDecoratorLibrary

```
@decorator
def function(arg):
    return "value"
```

is equivalent to

```
def function(arg):
    return "value"
function = decorator(function)
```

Example:

```
import functools

def decorator_maker_with_arguments(arg1, arg2, arg3):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(f_arg1, f_arg2):
        return func().upper()
    return wrapper
  return decorator

@decorator_maker_with_arguments(arg1, arg2, arg3)
def say_hi(f_arg1, f_arg2):
    "This will say hi"
    return 'hello there'

say_hi(f_arg1, f_arg2)
```
