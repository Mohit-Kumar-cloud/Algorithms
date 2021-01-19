# Function to determine if can be segmented into a space-separated
# sequence of one or more dictionary words
def wordBreak(dictionary, string="mohitkumar"):
 
    # return true if we have reached the end of the String,
    if not string:
        return True
 
    for i in range(1, len(string) + 1):
 
        # consider all prefixes of current String
        prefix = string[:i]
 
        # return true if prefix is present in the dictionary and remaining
        # also forms space-separated sequence of one or more
        # dictionary words
        if prefix in dictionary and wordBreak(dictionary, string[i:]):
            return True
 
    # return false if the can't be segmented
    return False
 
 
if __name__ == '__main__':
 
    # List of Strings to represent dictionary
    dictionary = ["self", "th", "is", "famous", "Word",
            "break", "b", "r", "e", "a", "k", "br",
            "bre", "brea", "ak", "problem"]
 
    # input String
    string = "Wordbreakproblem"
 
    if wordBreak(dictionary, string):
        print("String can be segmented")
    else:
        print("String can't be segmented")
 