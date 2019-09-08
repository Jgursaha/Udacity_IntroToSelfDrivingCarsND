import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

# Has two vectors as inputs and outputs the dot product of the 
# two vectors. First, it does element-wise
# multiplication and then sum the results. 

def dot_product(vector_one, vector_two):
    result = 0
    
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]

    return result

# Receives a matrix and a column number.
# The output should be the column in the form of a list
def get_column(matrix, column_number):
    column = []
    for r in range(len(matrix)):
        column.append(matrix[r][column_number])

    return column

# Receives a matrix and a row number.
# The output should be the row in the form of a list
def get_row(matrix, row):
    return matrix[row]

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # Implementation for a 1X1 matrix
        if self.h == 1:
            return self[0][0]
        
        # If execution has reached this part of the function, its a 2X2 matrix
        a = self[0][0]
        b = self[0][1]
        c = self[1][0]
        d = self[1][1]
        
        return (a*d) - (b*c)

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        trace = 0
        
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        rows = self.h
        
        for i in range(rows):
            trace += self[i][i]
        
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        row = []
        matrix_inverse = []
        matrix = self.g
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here

        # Implementation for a 1X1 matrix
        if self.h == 1:
            row.append(1/(matrix[0][0]))
            matrix_inverse.append(row)
            return Matrix(matrix_inverse)
        
        # If execution has reached this part of the function, its a 2X2 matrix
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
            
        factor = 1 / (a * d - b * c)
            
        inverse = [[d, -b],[-c, a]]

        for i in range(len(inverse)):
            for j in range(len(inverse[0])):
                inverse[i][j] = factor * inverse[i][j]

        return Matrix(inverse)
        
                         

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        row = []
        rows = self.h
        columns = self.w
        matrix = self.g
                         
        for i in range(columns):            
            for j in range(rows):
                row.append(matrix[j][i])
            matrix_transpose.append(row)
            row = []
            
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
                         
        # initialize matrix to hold the results
        matrixSum = []
        row = []
        rows = self.h
        columns = self.w
        matrix = self.g
    
        for i in range(rows):
            for j in range(columns):
                row.append(matrix[i][j] + other[i][j])
            matrixSum.append(row)
            row = []
    
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        matrix = self.g
        rows = self.h
        columns = self.w
        neg_matrix = []
        row = []
        
        for r in range(rows):
            for c in range(columns):
                row.append(self.g[r][c] * -1)
            neg_matrix.append(row)
            row = []
        
        
        return (Matrix(neg_matrix))

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        # initialize matrix to hold the results
        matrixSub = []
        row = []
        rows = self.h
        columns = self.w
        matrix = self.g
    
        for i in range(rows):
            for j in range(columns):
                row.append(matrix[i][j] - other[i][j])
            matrixSub.append(row)
            row = []
        
        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        
        #if (self.h != other.w):
        #    raise(ValueError, "Matrices are incompatible for the multiplacation function") 
        #   
        # TODO - your code here
        #
        # Store the number of rows in A and the number of columns in B.
        # This will be the size of the output matrix
        m_rows = self.h
        p_columns = other.w
        matrixA = self.g
        matrixB = other.g

        # empty list that will hold the product of AxB
        result = []

    
        # For loop within a for loop. The outside for loop will 
        # iterate through m_rows. The inside for loop will iterate 
        # through p_columns.
        for r in range(m_rows):
            # Accumulate the values of a row (reset each loop)
            row_result = []
            # Grab current A row
            rowA = get_row(matrixA, r)

            for c in range(p_columns):
                # Grab current B column
                colB = get_column(matrixB, c)
                # Calculate the dot product of the A row and the B column
                dot_prod = dot_product(rowA, colB)
                # And append to row_result
                row_result.append(dot_prod)

            # Add the row_result to the result matrix
            result.append(row_result)

        return Matrix(result)
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        rows = self.h
        columns = self.w
        result_matrix = []
        matrix = self.g
        row = []
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            for r in range(rows):
                for c in range(columns):
                    row.append(other * matrix[r][c])
                result_matrix.append(row)
                row = []
            return Matrix(result_matrix)
                    