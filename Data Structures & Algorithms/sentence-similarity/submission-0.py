class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        mem = defaultdict(set)
        for w1, w2 in similarPairs:
            mem[w1].add(w2)
            mem[w2].add(w1)

        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i]:
                if sentence1[i] not in mem or sentence2[i] not in mem:
                    return False
                if sentence1[i] not in mem[sentence2[i]]:
                    return False

        return True

        