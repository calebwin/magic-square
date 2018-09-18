import magic_square

def main():
    my_magic_square = magic_square.MagicSquare(3, 15)
    my_magic_square.set(0, 0, 5)
    print(my_magic_square.is_valid())
    my_magic_square.rotate(-27)
    print(my_magic_square)
    print(my_magic_square.center_of_mass())
    print(my_magic_square.moment_of_inertia())

if __name__ == '__main__':
    main()
