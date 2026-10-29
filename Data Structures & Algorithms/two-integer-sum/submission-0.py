class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for j in range(len(nums)):
            diff = target-nums[j]
            if diff in hash_table.keys():
                return [hash_table[diff], j]

            hash_table[nums[j]] = j 

        return []
    
        