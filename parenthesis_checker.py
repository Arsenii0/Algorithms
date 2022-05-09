# Function to check if brackets are balanced or not.
def isValid(str):

    symbols_map = {}
    symbols_map["{"] = "}"
    symbols_map["["] = "]"
    symbols_map["("] = ")"

    stack = []

    for symbol in str:
        if symbol in symbols_map.keys():
            stack.append(symbol)
        elif symbol in symbols_map.values():

            stack_last_index = len(stack) - 1

            if len(stack) == 0:
                return False

            elif symbols_map[stack[stack_last_index]] == symbol:
                stack.pop()
            else:
                return False

    return not stack


def main():
    print(isValid("{(())}}"))


if __name__ == "__main__":
    main()
