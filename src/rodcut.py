# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price,n,length): 
    val = [0 for x in range(n+1)] 
    val[0] = 0
	# Build the table val[] in bottom up manner and return 
	# the last entry from the table 
    for i in range(1, n+1): 
        max_val = INT_MIN 
        for j in length[0:i]:
            if j<=i:
                k=length.index(j) 
                max_val = max(max_val, price[k] + val[i-k-1]) 
            val[i] = max_val 

    return val[n] 

# Driver program to test above functions 
if __name__ == "__main__":
    arr = [1 ,6,18,22,28]
    length=[1,2,5,6,7]
    size = 11
    print("Maximum Obtainable Value is " + str(cutRod(arr,size,length))) 

