from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if len(merged) == 0:
                merged.append(interval)
            else:
                last_merged_interval = merged[-1]
                if interval[0] > last_merged_interval[1]:
                    merged.append(interval)
                elif interval[1] > last_merged_interval[1]:
                    merged[-1][1] = interval[1]
        return merged

def main():
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals2 = [[1, 4], [4, 5]]

    solution = Solution()

    print("Merged intervals for [[1, 3], [2, 6], [8, 10], [15, 18]]:", solution.merge(intervals1))
    print("Merged intervals for [[1, 4], [4, 5]]:", solution.merge(intervals2))

if __name__ == "__main__":
    main()

# Time complexity is O(n * logn) because of in place sorting. 
# Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(nlogn) complexity of sorting.

# If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(logn) space.