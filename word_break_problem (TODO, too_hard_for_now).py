# Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words.
# Note: From the dictionary B each word can be taken any number of times and in any order.


# Input:
# n = 12
# B = { "i", "like", "sam", "sung", "samsung", "mobile", "ice","cream", "icecream",
# "man", "go", "mango" }

# A = "ilikesamsung"
# Output: 1

# Explanation:
# The string can be segmented as
# "i like samsung" or "i like sam sung".


from collections import defaultdict


def wordBreak(line, dictionary, out=""):
    if not line:
        print(out)
        return True

    current_index = 1
    while current_index <= len(line):
        prefix = line[:current_index]

        # if prefix is present in the dictionary - recursively check all the suffixes
        if prefix in dictionary:
            suffix = line[current_index:]

            if wordBreak(suffix, dictionary, out + " " + prefix):
                return True

        current_index += 1

    return False


NOT_VISITED = -1

ABSENT = 0
PRESENT = 1


def wordBreakDynamicProgramming(
    line, dictionary, lookup_table=defaultdict(lambda: NOT_VISITED)
):
    line_size = len(line)

    if lookup_table[line_size] != NOT_VISITED:
        return lookup_table[line_size]

    if line_size == 0:
        lookup_table[line_size] = PRESENT
        return lookup_table[line_size]

    lookup_table[line_size] = line in dictionary

    current_index = 1
    while current_index <= line_size:
        prefix = line[:current_index]

        # if prefix is present in the dictionary - recursively check all the suffixes
        if prefix in dictionary:
            lookup_table[len(prefix)] = PRESENT
            suffix = line[current_index:]

            if wordBreakDynamicProgramming(suffix, dictionary, lookup_table):
                return True

        current_index += 1

    return lookup_table[line_size] == True

    # current_index = 1
    # while current_index <= len(line):
    #     prefix = line[:current_index]

    #     # if prefix is present in the dictionary - recursively check all the suffixes
    #     if prefix in dictionary:
    #         suffix = line[current_index:]

    #         if wordBreak(suffix, dictionary, out + " " + prefix):
    #             return True

    #     current_index += 1


def main():

    # True
    word_list = [
        "i",
        "like",
        "sam",
        "sung",
        "samsung",
        "mobile",
        "ice",
        "cream",
        "icecream",
        "man",
        "go",
        "mango",
    ]
    string_to_segment = "ilikesamsung"

    # True
    # word_list = ["abc", "de"]
    # string_to_segment = "abcde"

    # False
    # string_to_segment = "catsandog"
    # word_list = ["cats", "dog", "sand", "and", "cat"]

    # True
    # word_list = ["ab", "bcd", "b", "a"]
    # string_to_segment = "abcd"

    # True
    # word_list = [
    #     "self",
    #     "th",
    #     "is",
    #     "famous",
    #     "Word",
    #     "break",
    #     "b",
    #     "r",
    #     "e",
    #     "a",
    #     "k",
    #     "br",
    #     "bre",
    #     "brea",
    #     "ak",
    #     "problem",
    # ]
    # string_to_segment = "Wordbreakproblem"

    print(wordBreakDynamicProgramming(string_to_segment, word_list))


if __name__ == "__main__":
    main()
