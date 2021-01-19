# A Dynamic Programming based Python program for edit
# distance problem


def edit_distance(x, y):
	m=len(x)
	n=len(y)
	# Create a table to store results of subproblems
	ed = [[0 for k in range(n + 1)] for k in range(m + 1)]

	# Fill d[][] in bottom up manner
	for i in range(m + 1):
		for j in range(n + 1):

			# If first string is empty, only option is to
			# insert all characters of second string
			if i == 0:
				ed[i][j] = j # Min. operations = j

			# If second string is empty, only option is to
			# remove all characters of second string
			elif j == 0:
				ed[i][j] = i # Min. operations = i

			# If last characters are same, ignore last char
			# and recur for remaining string
			elif x[i-1] == y[j-1]:
				ed[i][j] = ed[i-1][j-1]

			# If last character are different, consider all
			# possibilities and find minimum
			else:
				ed[i][j] = 1 + min(ed[i][j-1],	 # Insert
								ed[i-1][j],	 # Remove
								ed[i-1][j-1]) # Replace

	return ed[m][n]


# Driver code
if __name__ == "__main__":
	str1 = "sham"
	str2 = "mohit"
	print(edit_distance(str1, str2))