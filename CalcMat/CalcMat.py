# Define a class to represent a 2x2 matrix
class Matrix:
    def __init__(self, elements):
        # elements is a list of lists, for example: [[1, 2], [3, 4]]
        self.values = elements

    # Overload the + operator for matrix addition
    def __add__(self, other):
        return Matrix([
            [self.values[0][0] + other.values[0][0], self.values[0][1] + other.values[0][1]],
            [self.values[1][0] + other.values[1][0], self.values[1][1] + other.values[1][1]]
        ])

    # Overload the - operator for matrix subtraction
    def __sub__(self, other):
        return Matrix([
            [self.values[0][0] - other.values[0][0], self.values[0][1] - other.values[0][1]],
            [self.values[1][0] - other.values[1][0], self.values[1][1] - other.values[1][1]]
        ])

    # Overload the * operator for matrix multiplication
    def __mul__(self, other):
        a = self.values
        b = other.values
        # Matrix multiplication formula for 2x2:
        return Matrix([
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ])

    # Display the matrix in a readable format
    def display(self):
        print(f"|{self.values[0][0]}  {self.values[0][1]}|")
        print(f"|{self.values[1][0]}  {self.values[1][1]}|")


# Function to read a 2x2 matrix from the user
def read_matrix(number):
    print(f"> Matrix {number}:")
    matrix = []
    for i in range(2):  # For each row
        row = []
        for j in range(2):  # For each column
            value = int(input(f"< Element {i},{j}: "))  # Read element at position (i, j)
            row.append(value)
        matrix.append(row)
    return Matrix(matrix)  # Return a Matrix object


# Main function: where the program starts
def main():
    # Read the first and second matrices
    matrix1 = read_matrix(1)
    matrix2 = read_matrix(2)

    # Display the matrices entered
    print("> Matrix 1:")
    matrix1.display()
    print("> Matrix 2:")
    matrix2.display()

    # Ask user for the operation they want to perform
    print("> Type 1 for addition,")
    print("        2 for subtraction,")
    print("        3 for multiplication")

    choice = input("< ")

    # Perform the chosen operation
    if choice == '1':
        result = matrix1 + matrix2
        print("> The sum of the two matrices is:")
        result.display()
    elif choice == '2':
        result = matrix1 - matrix2
        print("> The difference of the two matrices is:")
        result.display()
    elif choice == '3':
        result = matrix1 * matrix2
        print("> The product of the two matrices is:")
        result.display()
    else:
        # If input is not valid
        print("Invalid option.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
