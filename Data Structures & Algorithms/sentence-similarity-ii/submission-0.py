class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        encode = dict()
        cur = 0

        for pair in similarPairs:
            for w in pair:
                if w not in encode:
                    encode[w] = cur
                    cur += 1

        dsu = DSU(len(encode))

        for pair in similarPairs:
            w1, w2 = pair
            dsu.union(encode[w1], encode[w2])

        for i in range(len(sentence1)):
            w1 = sentence1[i]
            w2 = sentence2[i]

            if w1 == w2:
                continue

            if w1 not in encode or w2 not in encode:
                return False

            if dsu.find(encode[w1]) != dsu.find(encode[w2]):
                return False


        return True








        