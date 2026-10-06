class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        list_of_indices = []

        for index, elem in enumerate(nums):
            difference = target - elem
            if difference in dict_nums and dict_nums[difference] != index:
                list_of_indices.append(dict_nums[difference])
                list_of_indices.append(index)
                break
            else:
                dict_nums[elem] = index
        return list_of_indices
        