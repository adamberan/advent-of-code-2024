import itertools
with open('input0.txt') as file:
    matrix = [line.rstrip() for line in file]

m = len(matrix) # assume that the matrix is square

# part 1:
def check_element(i,j):
    x = [0] + [k for k in (-1,1) if 0 <= i + 3*k < m] # up or stay or down
    y = [0] + [k for k in (-1,1) if 0 <= j + 3*k < m] # left or stay or right
    directions = itertools.product(x,y) # includes 0,0 but it is ok
    words = ["".join([matrix[i + k*t][j + k*r] for k in range(4)]) for t,r in directions]
    return sum(w == 'XMAS' for w in words)
            
sum(check_element(i,j) for i in range(m) for j in range(m))

# part 2:
def check_element(i,j):
    u = "".join([matrix[i + k][j + k] for k in (-1,0,1)])
    v = "".join([matrix[i + k][j - k] for k in (-1,0,1)])
    return all([w in ["MAS", "SAM"] for w in [u,v]])

sum(check_element(i,j) for i in range(1, m - 1) for j in range(1, m - 1))