def create2d(row_count, col_count, value=None):
    """
    Create and return a 2D array having rowCount rows and colCount
    columns, with each element initialized to value.
    """
    a = [None] * row_count
    for row in range(row_count):
        a[row] = [value] * col_count
    return a


def dynamic_soln(string1, string2):
    x = string1
    y = string2
    m = len(string1)
    n = len(string2)
    opt = create2d(m + 1, n + 1, 0)
    opt_m = len(opt)
    opt_n = len(opt[0])
    # Fill the penalty of string x[i] with empty string
    for i in range(opt_n):
        opt[opt_m - 1][i] = (opt_n - i - 1) * 2

    # Fill the penalty of string y[i] with empty string
    for i in range(opt_m):
        opt[i][opt_n - 1] = (opt_m - i - 1) * 2

    # Filling rest of the matrix with dynamic programming formula:
    # opt[i][j] = min{opt[i+1][j+1] + 0/1, opt[i+1][j] + 2, opt[i][j+1] + 2} where 0 and 1 value depends on whether x[i] and y[j] are match or mismatch and 2 is penalty for gap
    for j in range(opt_n - 2, -1, -1):
        for i in range(opt_m - 2, -1, -1):
            if x[i] == y[j]:
                opt[i][j] = min(opt[i + 1][j + 1], opt[i + 1][j] + 2, opt[i][j + 1] + 2)
            else:
                opt[i][j] = min(opt[i + 1][j + 1] + 1, opt[i + 1][j] + 2, opt[i][j + 1] + 2)
    return opt[0][0]


def alignement(x, y, opt, opt_m, opt_n):
    i = 0
    j = 0
    while i != opt_m - 1 and j != opt_n - 1:

        if opt[i][j] == opt[i][j + 1] + 2:
            print("  -", y[j], "2")
            j = j + 1
        elif opt[i][j] == opt[i + 1][j] + 2:
            print(x[i], "  -", "2")
            i = i + 1
        if x[i] == y[j]:
            if opt[i][j] == opt[i + 1][j + 1]:
                print(x[i], " ", y[j], "0")
                i = i + 1
                j = j + 1
        else:
            if opt[i][j] == opt[i + 1][j + 1] + 1:
                print(x[i], " ", y[j], "1")
                i = i + 1
                j = j + 1

    if i < opt_m:
        for k in range(i, opt_m - 1):
            print(x[k], "  -", "2")
    if j < opt_n:
        for k in range(j, opt_n - 1):
            print("-  ", y[k], "2")
