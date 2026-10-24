class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        indices_list = []

        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        

        for j in range(len(nums_dict)):
            diff = target - nums[j]
            if diff in nums_dict and nums_dict[diff] != j:
                indices_list.append(j)
                indices_list.append(nums_dict[diff])
                break
        
        return indices_list