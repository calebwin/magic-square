import math

class MagicSquare:
    def __init__(self, n):
        self.n = n
        self.magic_constant = n * (math.pow(n, 2) + 1) / 2
        self.data = generate_matrix(n, n, -1)

    def __init__(self, n, magic_constant):
        self.n = n
        self.magic_constant = magic_constant
        self.data = generate_matrix(n, n, -1)

    def set_magic_constant(self, new_magic_constant):
        self.magic_constant = new_magic_constant

    def set(self, i, j, new_num):
        if i < 0 or i > len(self.data) - 1 or j < 0 or j > len(self.data[i]) - 1:
            raise ValueError("square positions out of bounds")

        self.data[i][j] = new_num

    def safe_set(self, i, j, new_num):
        if i < 0 or i > len(self.data) - 1 or j < 0 or j > len(self.data[i]) - 1:
            raise ValueError("square positions out of bounds")

        prev_num = self.data[i][j]
        self.data[i][j] = new_num

        if not self.is_valid():
            self.data[i][j] = prev_num
            raise ValueError("new magic square is invalid")

    def is_valid(self, *args):
        magic_constant = self.magic_constant
        if len(args) > 0:
            magic_constant = args[0]

        for i in range(0, self.n):
            row_total = 0
            for j in range(0, self.n):
                row_total += self.data[i][j]
            if row_total != magic_constant:
                return False

        for j in range(0, self.n):
            col_total = 0
            for i in range(0, self.n):
                row_total += self.data[i][j]
            if col_total != magic_constant:
                return False

        diagonal_total = 0
        for i in range (0, self.n):
            diagonal_total += self.data[i][i]
        for i in range (0, self.n):
            diagonal_total += self.data[self.n - 1 - i][i]
        if diagonal_total != magic_constant * 2:
            return False

        return True

    def rotate(self, num_rotations):
        rotate_matrix(self.data, num_rotations)

    def center_of_mass(self):
        total_product_position_x_weight = 0
        total_product_position_y_weight = 0
        total_weight = 0

        for i in range(0, self.n):
            for j in range(0, self.n):
                position_x = i + 1
                position_y = j + 1
                weight = self.data[i][j] / self.magic_constant

                total_weight += weight
                total_product_position_x_weight += position_x * weight
                total_product_position_y_weight += position_y * weight

        center_x_of_mass = math.floor(total_product_position_x_weight / total_weight - 1)
        center_y_of_mass = math.floor(total_product_position_y_weight / total_weight - 1)

        center_x_of_mass = max(0, center_x_of_mass)
        center_x_of_mass = min(self.n - 1, center_x_of_mass)
        center_y_of_mass = max(0, center_y_of_mass)
        center_y_of_mass = min(self.n - 1, center_y_of_mass)

        return (center_y_of_mass, center_x_of_mass)

    def moment_of_inertia(self):
        return math.pow(self.n, 2) * (math.pow(self.n, 4) - 1) / 12

    def __str__(self):
        matrix = ""
        for i in range(0, self.n):
            row = ""
            for j in range(0, self.n):
                row += str(self.data[i][j]) + " "
            matrix += row + "\n"
        return matrix

def generate_matrix(*args):
    n = args[0]
    m = args[1]
    num = args[len(args) - 1]
    data = {}
    if len(args) > 3:
        data = args[2]

    if data is {}:
        new_matrix = []
        for i in range(0, n):
            new_row = []
            for j in range(0, m):
                if i < len(data) and j < len(data[i]):
                    new_row.append(data[i][j])
                else:
                    new_row.append(num)
            new_matrix.append(new_row)
        return new_matrix
    else:
        new_matrix = []
        for i in range(0, n):
            new_row = []
            for j in range(0, m):
                new_row.append(num)
            new_matrix.append(new_row)
        return new_matrix

def rotate_matrix(data, num_rotations):
    n = len(data)
    num_rotations = abs(num_rotations) % 4
    for num in range(0, num_rotations):
        for i in range(0, int(n / 2)):
            for j in range(i, n - i - 1):
                temp = data[i][j]

                data[i][j] = data[j][n - 1 - i]

                data[j][n - 1 - i] = data[n - 1 - i][n - 1 - j]

                # move values from left to bottom
                data[n - 1 - i][n - 1 - j] = data[n - 1 - j][i]

                # assign temp to left
                data[n - 1 - j][i] = temp
