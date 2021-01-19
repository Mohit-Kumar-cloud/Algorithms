from io import StringIO
import sys
# A space optimized python3 program to
# print optimal parenthesization in 
# matrix chain multiplication.

def printParenthesis(m, j, i=0 ):

	# Displaying the parenthesis.
	if j == i:

		# The first matrix is printed as 
		# 'A', next as 'B', and so on
		print(chr(65 + j), end = "")
		return;
	else:
		print("(", end = "")

		# Passing (m, k, i) instead of (s, i, k)
		printParenthesis(m, m[j][i] - 1, i)

		# (m, j, k+1) instead of (s, k+1, j)
		printParenthesis(m, j, m[j][i])
		print (")", end = "" )


def matrixChainOrderPar(m,j,i=0):
    old_stdout= sys.stdout
    result= StringIO()
    sys.stdout=result
    printParenthesis(m, j, i)
    sys.stdout= old_stdout
    r=result.getvalue()
    return r
    


def matrixChainOrder(p):
    n=len(p)-1

	# Creating a matrix of order
	# n*n in the memory.
    m = [[0 for i in range(n)] 
            for i in range (n)]

    for l in range (2, n + 1):
        for i in range (n - l + 1):
            j = i + l - 1

			# Initializing infinity value.
            m[i][j] = float('Inf')
            for k in range (i, j):
                q = (m[i][k] + m[k + 1][j] +
                    (p[i] * p[k + 1] * p[j + 1]))
                if (q < m[i][j]):
                    m[i][j] = q

					# Storing k value in opposite index.
                    m[j][i] = k + 1
    return m


def matrixChainOrderCost(p):
    n=len(p)-1

	# Creating a matrix of order
	# n*n in the memory.
    m = [[0 for i in range(n)] 
            for i in range (n)]

    for l in range (2, n + 1):
        for i in range (n - l + 1):
            j = i + l - 1

			# Initializing infinity value.
            m[i][j] = float('Inf')
            for k in range (i, j):
                q = (m[i][k] + m[k + 1][j] +
                    (p[i] * p[k + 1] * p[j + 1]));
                if (q < m[i][j]):
                    m[i][j] = q

					# Storing k value in opposite index.
                    m[j][i] = k + 1
    return m[0][n-1]

# Driver Code
if __name__ == "__main__":
    arr = [40, 20, 30, 10, 30]


    m = matrixChainOrder(arr) # Forming the matrix m
    j=len(arr)-1

    print("Optimal Parenthesization is: "+ matrixChainOrderPar(m,j-1))

# Passing the index of the bottom left
# corner of the 'm' matrix instead of
# passing the index of the top right
# corner of the 's' matrix as we used
# to do earlier. Everything is just opposite
# as we are using the bottom half of the
# matrix so assume everything opposite even
# the index, take m[j][i].
    print("\nOptimal Cost is :", matrixChainOrderCost(arr))


