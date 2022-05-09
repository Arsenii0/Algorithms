# Longest Substring Without Repeating Characters

def longestUniqueSubstring(str):
    current_str = ""
    max_length = -1

    index = 0
    while index < len(str):
        current_letter = str[index]
        if current_letter in current_str:

            repeating_character_index = current_str.find(current_letter)
            # substring AFTER the repeating character (that's why + 1)
            current_str = current_str[repeating_character_index + 1 :]

        current_str += current_letter
        max_length = max(max_length, len(current_str))
        index += 1

    return max_length


def main():
    print(longestUniqueSubstring("abcdhcbayr"))


if __name__ == "__main__":
    main()
