class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        res = set(counter.values())
        return len(res) == 1