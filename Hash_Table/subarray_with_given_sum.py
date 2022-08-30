from collections import defaultdict

# if (sum_i % K == sum_j % K) -> sum_i - sum_j  = const*K -> divisible by K
# if (sum_i == sum_j - target sum) 
#     sum_j - sum_i = target_sum

#     sum_i == sum_i + targer_sum (sum_j)

def subArraySum(arr, n, Sum):
    Map = {}

    # Maintains sum of elements so far
    curr_sum = 0
    
    for i in range(0,n):
      
        # add current element to curr_sum
        curr_sum = curr_sum + arr[i]
        if curr_sum == Sum:
          
            print("Sum found between indexes 0 to", i)
            return
          
        if (curr_sum - Sum) in Map:
          
            print("Sum found between indexes", \
                   Map[curr_sum - Sum] + 1, "to", i)
             
            return
    
        Map[curr_sum] = i

arr = [10, 2, -2, -20, 10]
target_sum = -10
n = len(arr)

print(subArraySum(arr, n, target_sum))