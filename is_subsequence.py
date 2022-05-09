# Given two strings, find if first string is a subsequence of second


# Example 1:

# Input:
# A = AXY 
# B = YADXCP
# Output: 0 
# Explanation: A is not a subsequence of B
# as 'Y' appears before 'A'.
 

# Example 2:

# Input:
# A = gksrek
# B = geeksforgeeks
# Output: 1
# Explanation: A is a subsequence of B.

import string


def isSubSequenceRecursive(string1, string2, s1_size, s2_size):
    if s1_size == 0:
        return True
    if s2_size == 0:
        return False

    if string1[s1_size - 1] == string2[s2_size - 1]:
        return isSubSequenceRecursive(string1, string2, s1_size - 1, s2_size - 1)

    return isSubSequenceRecursive(string1, string2, s1_size, s2_size - 1)


def isSubSequencetIterative(string1, string2, s1_size, s2_size):
    if s1_size == 0:
        return True
    if s2_size == 0:
        return False

    s1_index = 0
    s2_index = 0

    while s1_index < s1_size and s2_index < s2_size:
        if string1[s1_index] == string2[s2_index]:
            s1_index+=1
        s2_index+=1
    
    return s1_index == s1_size


def main():
    # Driver program to test the above function
    string1 = "gksrek"
    string2 = "geeksforgeeks"
    
    if isSubSequencetIterative(string1, string2, len(string1), len(string2)):
        print ("Yes")
    else:
        print ("No")


if __name__ == "__main__":
    main()