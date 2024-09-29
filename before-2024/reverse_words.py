def reverse_string(str, left_index, right_index):
    while left_index < right_index:
        str[left_index], str[right_index] = str[right_index], str[left_index]
        left_index += 1
        right_index -= 1

    return str


def reverse_words(str):

    word_start_index = 0

    while word_start_index < len(str):
        while word_start_index < len(str) and str[word_start_index] == " ":
            word_start_index += 1

        if word_start_index == len(str):
            break

        word_end_index = word_start_index
        while word_end_index < len(str) and str[word_end_index] != " ":
            word_end_index += 1

        reverse_string(str, word_start_index, word_end_index - 1)

        word_start_index = word_end_index

    return reverse_string(str, 0, len(str) - 1)


def main():
    str = "arsen defines mouse button"

    # string in python are immutable
    str_list = list(str)

    reverse_words(str_list)

    # convert list back to string
    print("".join(str_list))


# reverse words inside an array without using extra characters
if __name__ == "__main__":
    main()
