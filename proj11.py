# The purpose of this project is to create a matrix class which can perform 
#   functions like addition subtraction and multiplication
# In order to do this, first create a function that initializes the rows
#   cols of the matrix 
# Then create a string function that can help print the matrix in a particular 
#   way
# Then create a function that can get the items from the matrix to help perform 
#   the functions 
# A function that sets the item to the perform the function is also created
# Then create functions like add, dot product, multiplication, equal, 
#   transpose and scalar multiplication.

class Matrix(object):
    def __init__(self,num_rows = 2,num_cols = 2 ):
        '''
            takes in 3 arguments 
            initializes the values of the columns and rows 
            prints an error
        '''
        
        self.num_rows = num_rows #initializes row and col 
        self.num_cols = num_cols
        #initializes the array by looping over row and col
        self.array = [[0] * self.num_cols for number in range(self.num_rows)]
        #if invalid row/ col 
        if self.num_rows < 0 or self.num_cols < 0:
            #raises an error
            raise ValueError("Matrix: Error, the dimensions must be \
                             positive integers!")
 
    def __str__(self):
        '''
            takes in one argument 
            returns a string representation of the matrix 
        '''
        string = "["
        #looping over the array 
        for rows in self.array:
            #sets the string equal to how it wants to print the matrix 
            string += str(rows).replace(",", "")
            string += "\n "
        #returns the representation of the matrix 
        return string[:-2] + "]"
        
    def __repr__(self):
        '''
            returns the same string as __str__
        '''
        #returns the __str__ 
        return self.__str__()
    
    def __getitem__(self, iijj):
        '''
            takes in 2 arguments 
            gets value from a matrix 
            returns the elements from the matrix 
        '''
        #checks if the all the condition for the matrix are met 
        #if not it raises an error 
        if type(iijj) == int:
            if iijj <= 0:
                raise IndexError("Matrix: Error, bad indexing!")
            elif self.num_rows < iijj:
                raise IndexError("Matrix: Error, index out of range!")
            #if condition met returns the ith and jth elements from matrix 
            return self.array[iijj - 1]                       

        elif type(iijj) == tuple:
            #states what i and j are 
            #iijj is a tuple of 2 items (row and col)
            i, j = iijj
            #checks if the all the condition for the matrix are met 
            #if not it raises an error 
            if type(i) == int and type(j) == int:
                if i <= 0 or j <= 0:
                    raise IndexError("Matrix: Error, bad indexing!")
                elif self.num_rows < i or self.num_cols < j:
                    raise IndexError("Matrix: Error, index out of range!")
                #if condition met returns the ith and jth element of matrix 
                return self.array[i - 1][j - 1] #-1 bc index 
            else:
                raise ValueError("Matrix: Error, the indices must be a \
                                 positive integer or a tuple of integers!")
        else:
            raise ValueError("Matrix: Error, the indices must be a positive \
                             integer or a tuple of integers!")
    
    
    def __setitem__(self, iijj, value):
        '''
            takes in three parameters 
            sets the value in a matrix 
            return the value 
        '''
        #checks if the all the condition for the matrix are met 
        #if not it raises an error
        if type(iijj) != tuple:
            raise ValueError("Matrix: Error, the indices must be a tuple \
                             of integers!")
        if type(iijj[0]) != int or type(iijj[1]) != int:
            raise ValueError("Matrix: Error, the indices must be a tuple \
                             of integers!")
        i, j = iijj #defines i and j 
        if i <= 0 or j <= 0:
            raise IndexError("Matrix: Error, bad indexing!")
        elif self.num_rows < i or self.num_cols < j:
            raise IndexError("Matrix: Error, index out of range!")
        if type(value) != int and type(value) != float:
            raise ValueError("Matrix: Error, You can only assign a float or \
                             int to a matrix!")
        #returns the value
        self.array[i -1][j - 1] = value 
    
    def __add__(self,B):
        '''
            takes in 2 arguments 
            adds the 2 matrix togther 
            return the calculated matrix 
        '''
        #checks if B is a matrix 
        if type(B) != Matrix:
            raise ValueError("Matrix: Error, you can only add a matrix to\
                             another matrix!")
            
        #checks if the dimensions of 2 matrics are same
        if self.num_rows != B.num_rows or self.num_cols != B.num_cols:
             raise ValueError("Matrix: Error, matrices dimensions must agree \
                              in addition!")
             
        #creates a new matrix C 
        matrix_c = Matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                #matrix c = matrix A + matrix B
                matrix_c[i+1,j+1] = self[i + 1, j+1] + B[i+1, j+1]
        #returns the calcuated matrix 
        return matrix_c
        
    def dot_product(self,L1,L2):
        '''
            =takes in 3 arguments 
            perfoms dot product on two matrices
            returns the multipled total
        '''
        #checks if the length of both the rows are the same 
        if len(L1) != len(L2):
            raise ValueError("Dot Product: must be same length")
            
        total = 0
        #calculates the total by multiplying the items in each row 
        for i in range(len(L1)):
            total += L1[i] * L2[i]
        #returns total 
        return total
        
    def __mul__(self,B):
        '''
            takes in two arguments 
            performs multiplication on 2 matrices
            returns the multiplied matrix
        '''
        #checks if B is a matrix 
        if type(B) != Matrix:
            raise ValueError("Matrix: Error, you can only multiply a matrix\
                             to another matrix!") 
            
        #checks if the rows and cols are the same length 
        if self.num_cols != B.num_rows:
             raise ValueError("Matrix: Error, matrices dimensions must agree \
                              in multiplication!")
        #creates a matrix c
        matrix_c = Matrix(self.num_rows, B.num_cols)
        #uses nested for loop to perform the mul function 
        for i in range(B.num_cols):
            new_row = []
            #appends to the new row using the matrix B 
            for j in range(B.num_rows):
                new_row.append(B[j+1, i+1])
            #calls in dot product to perform multiplication of the new row 
            for j in range(self.num_rows):
                dot = self.dot_product(new_row, self[j+1])
                #uses dot product to calculate matrix c 
                matrix_c[j+1, i+1] = dot
        #returns the calculated matrix 
        return matrix_c
    
    
    def transpose(self):
        '''
            takes in one argument 
            takes a row from a matrix and turns it into a column 
            returns the new converted matrix 
        '''
        #creates a new matrix 
        new_matrix = Matrix(self.num_cols, self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                #sets the rows in new matrix equal to the col of old matrix 
                # and vice versa 
                new_matrix[j+1, i+1] = self[i+1, j+1]
        #returns the new matrix 
        return new_matrix
    
    def __eq__(self,B):
        ''' 
            takes in 2 arguments
            checks if 2 matrices are equal or not 
            returns Boolean 
        '''
        #checks if B is a matrix and chekcs if both matrix are equal in length
        if type(B) == type(self) and self.num_rows == B.num_rows:
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    #checks if bother matrices are equal or not 
                    if self[i+1, j+1] != B[i+1, j+1]:
                        #false if not equal 
                        return False 
            return True
        else:
            #false if conditions are not met 
            return False 
        
        
    def __rmul__(self,scalar):
        '''
            takes in 2 arguments 
            multiplies a matrix with a scalar
            returns the multiplied matrix 
        '''
        #checks if the scalar is an integer
        if type(scalar) != int:
            raise ValueError("Matrix Error: scaler must be an int.")
        
        #creates a new matrix 
        new_matrix = Matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                #multiples the old matrix with the scalar and sets it equal to 
                # the new matrix
                new_matrix[i+1, j+1] = self[i+1, j+1] * scalar
        
        #returns the calculated matrix 
        return new_matrix   
