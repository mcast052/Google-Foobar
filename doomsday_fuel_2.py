import fractions

# Matrix multiplication only that returns only the first row
def matmul(f, r): 
    f_col = len(f[0])
    r_row = len(r)
    r_col = len(r[0])
    result = [] 
    
    if f_col == r_row:
        for i in range(r_col):
            val = 0
            for j in range(r_row):
                val = val + f[0][j]*r[j][i]
            result.append(val)
    return result

def matinv(m): 
    row = len(m) 
    col = len(m[0])
    # Checks if it is a square matrix
    if row == col:
        # Base case: 2x2 matrix
        if row == 2: 
            det = m[0][0]*m[1][1] - m[0][1]*m[1][0]
            inv = [ [ (1/det)*m[1][1], (-1/det)*m[0][1] ],
                    [ (-1/det)*m[1][0], (1/det)*m[0][0] ] ]
            return inv
        else: 
            #Create identity matrix
            inv = m
            I = [ [int(i==j) for i in range(len(m))] for j in range(len(m))]
            for i in range(len(inv)): 
                for j in range(len(inv[i])): 
                    inv[i].append(I[i][j])
            
            row2 = len(inv) 
            col2 = len(inv[0])
            for c in range(0, row2): 
                for c2 in range(c+1, row2): 
                    factor = inv[c2][c] / inv[c][c]
                    for r in range(c, col2): 
                        inv[c2][r] -= (inv[c][r] * factor)
            
            for c in range(row2-1, 0-1, -1): 
                factor = inv[c][c]
                for c2 in range(0, c): 
                    for r in range(col2-1, c-1, -1): 
                        inv[c2][r] -= inv[c][r] * inv[c2][c] / factor 
                inv[c][c] /= factor 
                
                for r in range(row2, col2): 
                    inv[c][r] /= factor 
    

    # Get inversion
    result = []
    for i in range(0, len(inv)): 
        arr = []
        for j in range(col, len(inv[i])): 
            arr.append(inv[i][j])
        result.append(arr)
        
    return result
    
def answer(m): 
    # Sort rows: Find terminal states and reorder matrix to put terminal states first 
    graph = []
    sortOrder = []
    for i in range(len(m)): 
        if sum(m[i]) == 0:  
            graph.append(m[i])
            sortOrder.append(i)
            
    numTerminal = len(graph) 
    
    # Find non-terminal states and append to matrix 
    # Get number of non-terminal states
    for i in range(len(m)): 
        if sum(m[i]) > 0: 
            graph.append(m[i])
            sortOrder.append(i)

    numStates = len(graph) - numTerminal
    
    # Base case
    if numStates == 0 and numTerminal == 1: 
        return [1, 1]
    
    # Sort columns by sortOrder array
    graph = [ [graph[j][i] for i in sortOrder] for j in range(len(graph)) ]

    # Make probabilities into fractions
    for i in range(len(graph)):
        rowSum = sum(graph[i])
        if rowSum > 0:
            for j in range(len(graph[i])):
                val = graph[i][j]
                if val > 0: 
                    graph[i][j] = fractions.Fraction(val, rowSum)
                    

    Q = [ [graph[i][j] for j in range(numTerminal, len(graph))] for i in range(numTerminal, len(graph))]

    R = [ [graph[i][j] for j in range(0, numTerminal)] for i in range(numTerminal, len(graph))]

    I = [ [int(i==j) for i in range(len(Q))] for j in range(len(Q))]
    
    # Calculate I - Q
    F = []
    for i in range(len(I)):
        arr = []
        for j in range(len(I[i])):
            arr.append(I[i][j] - Q[i][j])
        F.append(arr)
    
    # Calculate (I - Q)^-1
    F_inv = matinv(F)
    
    # Calculate fundamental matrix: F_inv*R
    FR = matmul(F_inv, R)
    
    # Break up into numerators and denominators
    result = [] 
    denom = []
    for elem in FR: 
        result.append(elem.numerator)
        denom.append(elem.denominator)
    
    # Get the least common denominator
    # lcd = 1
    # if len(FR) > 0: 
    lcd = denom[0]
    for i in denom[1:]:
        if lcd and i: 
            lcd = lcd * i / fractions.gcd(lcd, i)
            
    # Update output values to have common denominators
    for i in range(len(denom)): 
        if not denom[i] == 0: 
            result[i] = result[i] * (lcd / denom[i])

    # Append denominator to result list
    result.append(lcd)
    return result

m = [ [0, 2, 1, 0, 0], 
      [0, 0, 0, 3, 4],
      [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0]
    ]
    
m2 = [ [0, 1, 0, 0, 0, 1], 
      [4, 0, 0, 3, 2, 0],
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0]
    ]

#print(matmul(F, R))
A = [ [1, fractions.Fraction(-1, 2)], [fractions.Fraction(-4, 9), 1]]
# print A
# print(matinv(A))
# gauss_jordan(A)
# print A
print(answer(m2))
# print(answer(m))

# print(answer([
#         [1, 2, 3, 0, 0, 0],
#         [4, 5, 6, 0, 0, 0],
#         [7, 8, 9, 1, 0, 0],
#         [0, 0, 0, 0, 1, 2],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]
#     ]))
    
# print(answer([
#         [0]
#     ]))

# print(answer([
#         [1, 1, 1, 0, 1, 0, 1, 0, 1, 0], #s0
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s1
#         [1, 0, 1, 1, 1, 0, 1, 0, 1, 0], #s2
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s3
#         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], #s4
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s5
#         [1, 0, 1, 0, 1, 0, 1, 1, 1, 0], #s6
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s7
#         [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #s8
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #s9
#     ])) # States (in order): 1, 3, 5, 7, 9, 0, 2, 4, 6, 8