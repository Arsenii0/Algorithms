
# 0 is produced by 2 * 5 (prime numbers of factorial number)
# so we need to simply calculate how much 5 we have in prime numbers

# E.g 11 = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 = 3 * 2^3 * 5 * 6*7*8*9* 5*2 *11
# so we have two fives
def factorial_trailing_zeroes(number):
    result = 0
    
    while number >= 5:
        result += number // 5
        number = number // 5
        
    return result

print(factorial_trailing_zeroes(11))