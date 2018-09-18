## What it is
A magic square data structure for the Python programming language.

## How to use it
```python
my_magic_square = magic_square.MagicSquare(3, 15) # initialize a new 3X3 magic square with magic constant of 15

my_magic_square.set(0, 0, 5) # set the cell at position (0, 0) to 5

my_magic_square.is_valid() # False

my_magic_square.rotate(-27) # rotates magic square clockwise 27 times

print(my_magic_square)
print(my_magic_square.center_of_mass())
print(my_magic_square.moment_of_inertia())
```
