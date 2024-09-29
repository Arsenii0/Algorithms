def countSetBits(n):
    count = 0

    while (n != 0):
        # x & 1 produces a value that is either 1 or 0, depending on the least significant bit of x: if the
        #  last bit is 1, the result of x & 1 is 1; otherwise, it is 0. This is a bitwise AND operation.
        count += n & 1

        # x >>= 1 means "set x to itself shifted by one bit to the right". The expression evaluates to the new value of x after the shift.
        n >>= 1
    return count

    #Swap x, y. The XOR of two numbers x and y returns a number that has all the bits as 1 wherever bits of x and y differ.
    # x = x ^ y; // x now becomes 15 (1111)
    # y = x ^ y; // y becomes 10 (1010)
    # x = x ^ y; // x becomes 5 (0101)

def main():
    print(countSetBits(128))


if __name__ == "__main__":
    main()