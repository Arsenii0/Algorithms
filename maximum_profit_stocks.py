

from calendar import c


def rangeWithLast(start, end):
    return range(start, end + 1)


# 1. Max profit with infinite transactions allowed

# Example 1:
# Input:
# N = 10
# A[] = {23, 13, 25, 29, 33, 19, 34, 45, 65, 67}

# Output:
# (1 4) (5 9)
def profitWithInfiniteTransactionsAllowed(price):
    local_min_index = 0
    result = []

    current_index = 0
    while current_index < len(price):
        local_min = price[current_index]
        local_min_index = current_index
        current_index += 1
        for value in price[current_index:]:

            if value < local_min:
                local_min_index = current_index
                local_min = value
                current_index += 1
            else:
                break

        if local_min_index == len(price) - 1:
            break

        local_max_index = current_index
        local_max = price[local_max_index]

        current_index += 1
        for value in price[current_index:]:
            if value < local_max:
                break
            else:
                local_max_index = current_index
                local_max = value
                current_index += 1

        result.append((local_min_index, local_max_index))

    print(result)


# 2. Max Profit with only 1 transactions allowed
# Maximum difference between two elements such that larger element appears after the smaller number

# Input : arr = {2, 3, 10, 6, 4, 8, 1}
# Output : 8
# Explanation : The maximum difference is between 10 and 2.

# Algorihm:
# 1) Maximum difference found so far (max_diff). 
# 2) Minimum number visited so far (min_element).

def maxProfitWIthOnlyOneTransactionAllowed(arr):

    # TODO add arr size verifications

    maximum_diff_so_far = arr[1] - arr[0]
    min_element_so_far = arr[0]

    current_index = 1
    while current_index < len(arr) - 1:
        curr_diff = arr[current_index] - min_element_so_far
        if curr_diff > maximum_diff_so_far:
            maximum_diff_so_far = curr_diff
        
        if arr[current_index] < min_element_so_far:
            min_element_so_far = arr[current_index]

        current_index+=1

    print(maximum_diff_so_far)


# Example:
# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75 
# Buy at 10, sell at 22, 
# Buy at 5 and sell at 80

# Algorihm:
# 1) Create profit_back array which stores maximum profit on i-position [n...0].
#    Note - profit_back need to be traversed in reversed order because buy -> sell -> buy -> sell 
# 2) Create profit_forward array which stores maximum profit on i-position [0..n]
# 3) find maximum profit_back[i] + profit_front[i]
def maxProfitWIthTwoTransactionAllowed(arr):
    arr_size = len(arr)
    if arr_size < 2:
        return 0

    profit_back = [0] * arr_size
    profit_front = [0] * arr_size

    # calculate profit_back:
    max_price = arr[arr_size - 1]
    index_back = arr_size - 2

    # TODO ArsenP : check nicer loop (for index_back in range(n-2, 0, -1):)
    while index_back > -1:
        profit_back[index_back] = max(profit_back[index_back + 1], max_price - arr[index_back])

        max_price = max(max_price, arr[index_back])
        index_back-=1

    # calculate profit_front:
    min_price = arr[0]
    index_front = 1
    while index_front < arr_size:
        profit_front[index_front] = max(profit_front[index_front - 1], arr[index_front] - min_price)

        min_price = min(min_price, arr[index_front])
        index_front+=1

    profit_with_two_transactions_each_day = []
    for i in range(0, arr_size):
        profit_with_two_transactions_each_day.append(profit_front[i] + profit_back[i])

    print(max(profit_with_two_transactions_each_day))


def main():
    A = [2, 30, 15, 10, 8, 25, 80]
    print("\n1. Infinite transaction allowed")
    profitWithInfiniteTransactionsAllowed(A)

    print("\n2. Only one transaction allowed")
    B = [2, 3, 10, 6, 4, 8, 1]
    maxProfitWIthOnlyOneTransactionAllowed(B)

    print("\n3. Only two transactions allowed")
    C = [10, 22, 5, 75, 65, 80]
    maxProfitWIthTwoTransactionAllowed(C)


if __name__ == "__main__":
    main()
