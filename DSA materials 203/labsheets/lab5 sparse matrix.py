"""
1. Implement a class to represent a sparse matrix using coordinate list representation

(a)Initialize a sparse matrix with a given number of rows and columns.

(b)Insert elements into the sparse matrix.

(c )Display the sparse matrix.

2. Write a function to add two sparse matrices and return the resulting sparse matrix. Ensure that the matrices being added are compatible for addition.

3. Implement a function to find and display the transpose of a given sparse matrix.

4. Write a function to find the inverse of a sparse matrix if it is invertible

Block Matrix Representation

5. Implement a class to represent a block matrix. The matrix should be divided into square blocks.

(a)Initialize a block matrix with a given size and block size.

(b)Insert elements into the block matrix.

(c)Display the block matrix.

6.  Conformal Decomposition

Write a function to perform conformal decomposition on a given matrix. Decompose the matrix into a sum of matrices representing its diagonal and off-diagonal blocks.

Example:

Input Matrix:

[[1 2 3]

 [4 5 6]

 [7 8 9]]


Diagonal Blocks:

[[1 0 0]

 [0 5 0]

 [0 0 9]]


Off-diagonal Blocks:

[[0 2 3]

 [4 0 6]

 [7 8 0]]
 """

class SparseMatrix:
     def __init__(self, rows, cols, nzs):
          self._data = [[rows, cols, nzs]]
          self._nzs = nzs

     def __setitem(self, key, value):
          if len(self._data)+1==self._nzs:
               print("Insertion Limit Reached: No other elements can be added")
               return
          else:
               self._data.append([key[0], key[1], value])
               self._data = sorted(self._data)
     def __add__(self, other):
          if self._data[0][:2] == other._data[0][:2]:
               data = [self._data[0]]
               selfdata = set(tuple(i) for i in self._data[1:])
               otherdata = set(tuple(i) for i in other._data[1:])
               newinstance = SparseMatrix(self._data[0][0], self._data[0][1], len(selfdata.union(otherdata)))
               for i in sorted(selfdata.union(otherdata)):
                    newinstance[i[:2]] = i[2]
          else:
               print(f"Dimension Error: the Dimensions ({self._data[0][0]}, {self._data[0][1]}) and ({other._data[0][0]}, {other._data[0][1]}) doesn't match")














