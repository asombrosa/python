
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index_by_value = {}  # value -> index

    for i, x in enumerate(nums):
        need = target - x
        if need in index_by_value:
            return [index_by_value[need], i]
        index_by_value[x] = i

    # If problem guarantees a solution, we won't reach here.
    raise ValueError("No two sum solution")
#https://neetcode.io/problems/two-integer-sum/question