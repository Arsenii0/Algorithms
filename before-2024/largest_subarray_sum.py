def maxSubArraySum(array):
    if not array:
        return 0
    
    result_max = array[0]
    current_max = 0

    current_index = 1
    while current_index < len(array):
        current_max = current_max + array[current_index]
        if result_max < current_max:
            result_max = current_max
        if current_max < 0:
            current_max = 0

        current_index+=1

    return result_max

def maxSubArraySumDynamicProgramming(array):
    if not array:
        return 0
    
    result_max = array[0]
    current_max = array[0]

    current_index = 1
    while current_index < len(array):
        current_max = max(array[current_index], array[current_index] + current_max)
        result_max = max(result_max, current_max)

        current_index+=1

    return result_max



def main():
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubArraySumDynamicProgramming(array))


if __name__ == "__main__":
    main()