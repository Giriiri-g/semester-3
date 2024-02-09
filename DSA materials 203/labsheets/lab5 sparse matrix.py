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
     def __init__(self, rows, cols):
          self._data = [[rows, cols, 0]]

     def __setitem__(self, key, value):
          if (key[0] > self._data[0][0]-1) or (key[1] > self._data[0][1]-1):
               print(f"Invalid Indexing: {key} for size of {tuple(self._data[0][:2])}")
          data = [[0 for i in range(self._data[0][1])] for i in range(self._data[0][0])]
          for i in self._data[1:]:
               data[i[0]][i[1]] = i[2]
          if data[key[0]][key[1]] == 0:
               self._data[0][2]+=1
          del data
          self._data.append([key[0], key[1], value])
          header = self._data[0]
          data = sorted(self._data[1:])
          self._data = [header]
          for i in data:
               self._data.append(i)
          

     def __getitem__(self, key):
          if (key[0] > self._data[0][0]-1) or (key[1] > self._data[0][1]-1):
               print(f"Invalid Indexing: {key} for size of {(self._data[0][0]-1, self._data[0][1]-1)}")
               return None
          for i in self._data:
               if (i[0], i[1]) == key:
                    return i[2]
          return 0

     def __add__(self, other):
          if self._data[0][:2] == other._data[0][:2]:
               data = self._data[0]
               selfdata = set(tuple(i) for i in self._data[1:])
               otherdata = set(tuple(i) for i in other._data[1:])
               newinstance = SparseMatrix(self._data[0][0], self._data[0][1], len(selfdata.union(otherdata)))
               newinstance[tuple(data[:2])] = data[2]
               for i in sorted(selfdata.union(otherdata)):
                    newinstance[i[:2]] = i[2]
               return newinstance
          else:
               print(f"Dimension Error: the Dimensions ({self._data[0][0]}, {self._data[0][1]}) and ({other._data[0][0]}, {other._data[0][1]}) doesn't match")

     def __str__(self):
          res=""
          data = [[0 for i in range(self._data[0][1])] for i in range(self._data[0][0])]         #[[0]*self._data[0][1]]*self._data[0][0]
          for i in self._data[1:]:
               data[i[0]][i[1]] = i[2]
          for i in data:
               for j in i:
                    res+="{:>5}".format(j)
               res+="\n"
          return res[:-1]













