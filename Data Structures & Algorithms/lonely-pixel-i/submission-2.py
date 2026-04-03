class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [0 for _ in range(len(picture))]
        cols = [0 for _ in range(len(picture[0]))]

        answer = 0

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B" and rows[i] == 1 and cols[j] == 1:
                    answer += 1

        return answer