class SparseMatrix:
    def __init__(self, rows, cols):
        self.__data = [[rows, cols, 0]]

    def __setitem__(self, key, value):
        if (key[0] > self.__data[0][0]-1) or (key[1] > self.__data[0][1]-1):
            print(f"Invalid Indexing: {key} for size of {tuple(self.__data[0][:2])}")
        if self[key] == 0:
            self.__data[0][2]+=1
            self.__data.append([key[0], key[1], value])
            header = self.__data[0]
            data = sorted(self.__data[1:])
            self.__data = [header]
            for i in data:
                self.__data.append(i)
        else:
            header = self.__data[0]
            self.__data = [[i[0], i[1], value] if tuple(i[:2]) == key else i for i in self.__data[1:]]
            self.__data.insert(0, header)
          

    def __getitem__(self, key):
        if (key[0] > self.__data[0][0]-1) or (key[1] > self.__data[0][1]-1):
            print(f"Invalid Indexing: {key} for size of {(self.__data[0][0]-1, self.__data[0][1]-1)}")
            return None
        for i in self.__data[1:]:
            if (i[0], i[1]) == key:
                return i[2]
        return 0

    def __add__(self, other):
        if self.__data[0][:2] == other.__data[0][:2]:
            header = self.__data[0]
            newinstance = SparseMatrix(header[0], header[1])
               
            for i in self.__data[1:]:
                newinstance[(i[0], i[1])] = i[2]
            for i in other.__data[1:]:
                newinstance[(i[0], i[1])] = newinstance[(i[0], i[1])] + i[2]
            return newinstance
        else:
            print(f"Dimension Error: the Dimensions ({self.__data[0][0]}, {self.__data[0][1]}) and ({other.__data[0][0]}, {other.__data[0][1]}) doesn't match")

    def __str__(self):
        res=""
        data = [[0 for i in range(self.__data[0][1])] for i in range(self.__data[0][0])]         #[[0]*self.__data[0][1]]*self.__data[0][0]
        for i in self.__data[1:]:
            data[i[0]][i[1]] = i[2]
        for i in data:
            for j in i:
                res+="{:>5}".format(j)
            res+="\n"
        return res[:-1]

    def display(self):
        print("+-----+-----+-----+-----+")
        print("| Ind | Row | Col | Val |")
        print("+-----+-----+-----+-----+")
        for i, val in enumerate(self.__data):
            if i==0:
                print("| {:<3} | {:<3} | {:<3} | {:<3} |".format(i+1, val[0], val[1], val[2]))
                print("+-----+-----+-----+-----+")
                continue
            print("| {:<3} | {:<3} | {:<3} | {:<3} |".format(i+1, val[0]+1, val[1]+1, val[2]))
        print("+-----+-----+-----+-----+")



sp = SparseMatrix(5, 5)
sp[(1, 2)] = 3
sp[(4, 1)] = 1
sp[(2, 0)] = 4
sp[(3, 3)] = 12
sp2 = SparseMatrix(5, 5)
sp2[(1, 3)] = 5
sp2[(4, 1)] = 12
sp2[(2, 0)] = 3
sp2[(3, 4)] = 8
sp2[(3, 1)] = 46
sp2[(2, 2)] = 9

sp3 = sp + sp2
sp.display()
sp2.display()
sp3.display()