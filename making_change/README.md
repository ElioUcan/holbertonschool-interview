# Making Change

## Description
This project focuses on the classic Coin Change problem, frequently encountered in technical interviews. The objective is to determine the fewest number of coins needed to meet a given total amount from a given set of coin denominations.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code style adheres to PEP 8 (version 1.7.x)
- All files are executable

## Tasks

### 0. Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: `def makeChange(coins, total)`
- Return: Fewest number of coins needed to meet `total`
  - If `total` is `0` or less, return `0`
  - If `total` cannot be met by any number of coins in possession, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution's runtime will be evaluated in this task

### Example
```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

$ ./0-main.py
7
-1
```
