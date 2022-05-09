# Longest Substring Without Repeating Characters

def isPowerOfTwo(number):
    if number == 0:
        return False

    while (number != 1):
        if (number % 2 != 0):
            return False
        
        number = number // 2

    return True

def main():
    print(isPowerOfTwo(62))


if __name__ == "__main__":
    main()
