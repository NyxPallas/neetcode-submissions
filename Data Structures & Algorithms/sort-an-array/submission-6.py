def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket_list = []
        min_val = min(nums)
        max_val = max(nums)
        for i in nums:
            bucket_list.append([])
        for j in nums:
            if len(nums) == 1:
                bucket_list[0].append(j)
            if min_val == max_val:
                return nums
            else:
                num_index = int((j - min_val) / (max_val - min_val) * (len(nums) - 1))
                bucket_list[num_index].append(j)
        
        bucket_list = [n for n in bucket_list if len(n) > 0]
        for i in bucket_list:
            insertionSort(i)
        sorted_list = []
        for bucket in bucket_list:
            for elem in bucket:
                sorted_list.append(elem)
        return sorted_list

    
    
        