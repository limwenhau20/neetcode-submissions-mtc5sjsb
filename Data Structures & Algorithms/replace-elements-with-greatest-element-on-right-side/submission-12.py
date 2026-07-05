class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        len_arr = len(arr)
        output = []
        for i, num in enumerate(arr):
            if i == len_arr - 1:
                output.append(-1)
            else:
                output.append(max(arr[i+1:]))

        return output