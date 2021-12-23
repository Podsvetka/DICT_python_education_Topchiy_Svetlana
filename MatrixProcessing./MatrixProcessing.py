while True:
    while True:
        C_1 = list(input("Please, input line and columns matrix A: \n"))
        column_1 = int(C_1[0])
        line_1 = int(C_1[2])
        matrix_1 = []
        line_true_a = 0
        for i in range(column_1):
            matrix_1.append(list(map(int, input().split())))
        for height in range(len(matrix_1)):
            if len(matrix_1[height]) == line_1:
                line_true_a += 1
        if line_true_a == column_1:
            break
        else:
            print("Please, try again")

    while True:
        C_2 = list(input("Please, input line and columns matrix B: \n"))
        column_2 = int(C_2[0])
        line_2 = int(C_2[2])
        matrix_2 = []
        line_true_b = 0
        for i in range(column_2):
            matrix_2.append(list(map(int, input().split())))
        for height in range(len(matrix_2)):
            if len(matrix_2[height]) == line_2:
                line_true_b += 1
        if line_true_b == column_2:
            break
        else:
            print("Please, try again")

    if column_1 == column_2 and line_1 == line_2:
        result = []
        for i in range(column_1):
            result.append([0]*line_2)
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                result[i][j] = matrix_1[i][j] + matrix_2[i][j]
        for matrix_result in range(len(result)):
            print(*result[matrix_result])
            break
    else:
        print("error")