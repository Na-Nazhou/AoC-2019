# Advent of Code 2019

Language: `Python3`

Testing:

`python3 day1pt1.py < data.in > data.out`

`diff data.out expected1.out`

Increments: Day 2, 5, 7, 9, 11 (related to day 3 and day 8)

### Notes

- functions
  - \*args: tuple
  - \*\*kwargs: dict
- dictionary
  - for key, value in dict.items():
  - del dict[key], dict.pop(key)
- list
  - for idx, elem in enumerate(list)
  - sorted(list)
  - list comprehension: create new list
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

- others
  - dir, help
