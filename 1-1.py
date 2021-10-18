from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic={}   ##key儲存nums裡的數  value 儲存下標
        len_nums=len(nums)
        for i in range(len_nums):
            if target-nums[i] in dic:
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]]=i
            
