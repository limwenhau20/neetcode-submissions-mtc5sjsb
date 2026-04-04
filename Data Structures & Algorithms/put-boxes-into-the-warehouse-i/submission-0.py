class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        wh = []

        cur = math.inf

        for w in warehouse:
            if w <= cur:
                wh.append(w)
                cur = w
            else:
                wh.append(cur)

        boxes.sort(reverse=True)

        answer = 0
        j = 0
        i = 0

        while i < len(boxes) and j < len(warehouse):
            while i < len(boxes) and boxes[i] > warehouse[j]:
                i += 1

            if i < len(boxes):
                i += 1
                j += 1
                answer += 1

        return answer