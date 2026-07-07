class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #### My solution O(n2)
        len_arr = len(arr)
        output = []
        for i, num in enumerate(arr):
            if i == len_arr - 1:
                output.append(-1)
            else:
                output.append(max(arr[i+1:]))

        return output

        len_arr = len(arr)
        output = [0] * len_arr
        rightMax = -1
        for i in range(len_arr-1, -1, -1):
            output[i] = rightMax
            rightMax = max(rightMax, arr[i])
        return output
