# Dynamic Programming implementation of LCS problem 

def lcs_len(X , Y): 
	# find the length of the strings 
	m = len(X) 
	n = len(Y) 

	# declaring the array for storing the dp values 
	L = [[None]*(n+1) for i in range(m+1)] 

	"""Following steps build L[m+1][n+1] in bottom up fashion 
	Note: L[i][j] contains length of LCS of X[0..i-1] 
	and Y[0..j-1]"""
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j] , L[i][j-1]) 

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
	return L[m][n] 
#end of function lcs 


# Dynamic Programming implementation of LCS problem 

def lcs_matrix(X , Y): 
	# find the length of the strings 
	m = len(X) 
	n = len(Y) 

	# declaring the array for storing the dp values 
	L = [[None]*(n+1) for i in range(m+1)] 

	"""Following steps build L[m+1][n+1] in bottom up fashion 
	Note: L[i][j] contains length of LCS of X[0..i-1] 
	and Y[0..j-1]"""
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j] , L[i][j-1]) 

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
	return L


def lcs(X , Y):
    L=lcs_matrix(X,Y) 
    index=lcs_len(X,Y)
    lcs=[""] *(index+1)
    lcs[index]=""
    i=len(X)
    j=len(Y)
    while i>0 and j>0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
    return lcs



def main(): 
    X = ""
    Y = ""
    print ("Length of LCS is ", lcs_len(X, Y))
    print ("LCS is \n"+"".join(lcs(X, Y)))
if __name__ == "__main__":
    main()