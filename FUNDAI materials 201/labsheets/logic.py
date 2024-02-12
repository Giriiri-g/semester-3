# logic.py

# Function to create logical symbols for the domain
class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f'Square({self.row}, {self.col})'

class Mark:
    def __init__(self, mark):
        self.mark = mark

    def __eq__(self, other):
        return self.mark == other.mark

    def __repr__(self):
        return f'Mark({self.mark})'

# Function to create logical symbols for the domain
def expr(name):
    return name



# Function to check if a given square and mark are in a situation
def expr_in_situation(situation, square, mark):
    return expr('In')(square, situation) & expr('Mark')(square, mark)



