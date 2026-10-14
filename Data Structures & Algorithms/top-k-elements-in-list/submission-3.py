class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_dict = {}
        for num in nums:
            bucket_dict[num] = bucket_dict.get(num, 0) + 1
        sorted_dict = dict(reversed(sorted(bucket_dict.items(), key=lambda item: item[1])))
        elem_list = []

        for i in sorted_dict:
            if len(elem_list) == k:
                break
            else:
                elem_list.append(i)
        return elem_list

        