import ast
import itertools
import copy
from math import floor, ceil

def matrix_input(range):
    line = range
    matrix = []
    for i in range(line):
        t = []
        for j in input().split():
            if j != " ":
                t.append(ast.literal_eval(j))
        matrix.append(t)
    return matrix
def matrix_print(result, range, column):
    line, columns = range, column
    for i in range(line):
        for j in range(columns):
            print(result[i][j], end=' ')
        print()
def matrix_sum(m1, m2, range, col):
    line, columns = range, col
    append = []
    for i in range(line):
        temp = []
        for j in range(columns):
            if result[i][j] == -0.0:
                print(0, end=" ")
            elif type(result[i][j]) == int or result[i][j] == 0:
                print(result[i][j], end=" ")
            elif type(result[i][j]) == float and result[i][j] != 0:
                if result[i][j] > 0:
                    print(floor(result[i][j] * 100) / 100.0, end=" ")
                else:
                    print(ceil(result[i][j] * 100) / 100.0, end=" ")
    print()

def matrix_number(m1, number_m):
    multiply = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a[0])):
            temp.append(m1[i][j] * number_m)
        multiply.append(temp)
    return multiply
def matrix_element(l1, l2):
    result = 0
    for i in range(len(l1)):
        result += l1[i] * l2[i]
    return result

def matrix_two(m1, m2):
    value = [[0 for range in range(len(m2[0]))] for column in range(len(m1))]
    for i in range(len(m1)):
        l1 = m1[i]
        for j in range(len(m2[0])):
            l2 = [m2[x][j] for x in range(len(m2))]
            value_range = matrix_element(l1, l2)
            value[i][j] = value_range
    return value

def transe_main_diag(math):
    return list(itertools.zip_longest(*math))


def transe_side_diag(math):
    new_matrix = [[math[j][i] for j in range(len(math))] for i in range(len(math[0]) - 1, -1, -1)]
    result = []
    for i in range(len(new_matrix[0])):
        new_matrix[i] = new_matrix[i][::-1]
        result.append(new_matrix[i])
    return result


def transe_ver_line(math):
    new_matrix = [[math[j][i] for j in range(len(math))] for i in range(len(math[0]) - 1, -1, -1)]
    result = list(itertools.zip_longest(*new_matrix))
    return result


def transe_hor_line(math):
    result = list(itertools.zip_longest(*math[::-1]))
    result = list(itertools.zip_longest(*result))
    return result

def min(matx_min, i, j):
        return [row[:j] + row[j + 1:] for row in (matx_min[:i] + matx_min[i + 1:])]


def min_transe(math):
    determ = det(math)
    if len(math) == 2:
        return [[math[1][1] / determ, -1 * math[0][1] / determ],
                [-1 * math[1][0] / determ, math[0][0] / determ]]
    cofactors = []
    for r in range(len(math)):
        case = []
        for j in range(len(math)):
            minored = min(math, r, j)
            case.append(((-1) ** (r + j)) * det(minored))
        cofactors.append(case)
    cofactors = transe_main_diag(cofactors)
    for i in range(len(cofactors)):
        cofactors[i] = list(cofactors[i])
    for r in range(len(cofactors)):
        for j in range(len(cofactors)):
            cofactors[r][j] = int(cofactors[r][j]) / determ
    return cofactors

def det(matx_det):
    if len(matx_det) == 2:
        return matx_det[0][0] * matx_det[1][1] - matx_det[0][1] * matx_det[1][0]
    determ = 0
   for i in range(len(matx_det)):
        determ += ((-1) ** i) * matx_det[0][i] * det(min(matx_det, 0, i))
    return determ

while True:
    print("""1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
0. Exit""")
    choice = int(input("Your choice:"))
    choice = int(input('Your choice:'))
    if choice == 1:
        m, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matrix_input(m)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matrix_input(p)
        if m != p and n != q:
            print("The operation cannot be performed.")
        else:
            c = matrix_sum(a, b, m, n)
            matrix_print(c, m, n)
    elif choice == 2:
        m, n = map(int, input("Enter size of matrix:").split())
        print("Enter matrix:")
        a = matrix_input(m)
        number = float(input("Enter constant:"))
        c = matrix_number(a, number)
        print("The result is:")
        matrix_print(c, m, n)
    elif choice == 3:
        m, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = matrix_input(m)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = matrix_input(p)
        c = matrix_two(a, b)
        print("The result is:")
        matrix_print(c, m, q)
    elif choice == 4:
        print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line.""")
        choice = int(input("Your choice:"))
        if choice == 1:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(m)
            c = transe_main_diag(a)
            print('The result is:')
            matrix_print(c, n, m)
        elif choice == 2:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(m)
            c = transe_side_diag(a)
            print('The result is:')
            matrix_print(c, n, m)
        elif choice == 3:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(m)
            c = transe_ver_line(a)
            print('The result is:')
            matrix_print(c, m, n)
        elif choice == 4:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(m)
            c = transe_hor_line(a)
            print('The result is:')
            matrix_print(c, m, n)
        elif choice == 5:
            m, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matrix_input(m)
            c = det(a)
            print('The result is:')
            print(c)
        elif choice == 6:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = matx_input(matrix)
            c = det(a)
            print(c)
            if c != 0:
                d = min_transe(a)
                print('The result is:')
                matrix_print(d, matrix, n)
            else:
                print("This matrix doesn't have an inverse.")
        elif choice == 0:
            break