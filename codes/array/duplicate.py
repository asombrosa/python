#https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
def hasDuplicate(self, nums: List[int]) -> bool:
            
    return len(nums)!= len(set(nums))