import random
from operator import itemgetter


class Cell(object):
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val

    def print_cell(self):
        print self.val,

    def get_val(self):
        return self.val

    def get_coords(self):
        return self.row, self.col


class Matrix(object):
    def __init__(self, m, n):
        self.matrix = [[Cell(row, column, random.randint(-20, 20)) for column in range(n)] for row in range(m)]
        for row in self.matrix:
            for c in row:
                c.print_cell()
            print "\n"

    def calculate_sum(self, c_start, c_end):
        m1, n1 = c_start.get_coords()
        m2, n2 = c_end.get_coords()
        sub_matrix_sum = 0
        for i in range(m1, m2+1):
            for j in range(n1, n2+1):
                sub_matrix_sum += self.matrix[i][j].get_val()
        return sub_matrix_sum

    def calc_all_sums(self):
        all_sums = []
        for row in self.matrix:
            for startCell in row:  # for each cell in each row of the matrix
                for row1 in self.matrix:
                    for endCell in row1:
                        all_sums.append((startCell.get_coords(), endCell.get_coords(), self.calculate_sum(startCell, endCell)))
        return all_sums


    #    We are given an MxN matrix

if __name__ == "__main__":
    dimensions = []
    s = raw_input()
    dimensions = s.split(',')
    m = int(dimensions[0])
    n = int(dimensions[1])

    matrix = Matrix(m, n)
    l = []
    l = matrix.calc_all_sums()
    l = sorted(l, key=itemgetter(2))
    for i in l:
        print i
    print "largest sum submatrix is defined by cells %s and %s and sums up to %s" %(str(l[-1][0]), str(l[-1][1]), str(l[-1][2]))