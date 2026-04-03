class Solution:
    def rearrangeString(self, s: str, k: int) -> str:


        counter = Counter(s)

        q = deque([])

        hp = []

        for key, value in counter.items():
            heapq.heappush(hp, (-value, key))

        answer = []

        while len(answer) < len(s):
            if q and q[0][0] <= len(answer):
                _, freq, al = q.popleft()
                heapq.heappush(hp, (freq, al))

            if not hp:
                return ""
            
            freq, al = heapq.heappop(hp)
            answer.append(al)

            if freq + 1 < 0:
                q.append((len(answer)+k-1, freq + 1, al))

        return "".join(answer)