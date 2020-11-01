class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or len(words) < 2:
            return True
        index ={c:i for i, c in enumerate(order, start = 1)}
        prev_val = 0
        max_len = len(words[0])
        for word in words[1:]:
            max_len = max(max_len, len(word))
        for word in words:
            val = 0
            count = 0
            for c in word:
                count += 1
                val = val * 26 + index[c]
            while count < max_len:
                count += 1
                val *= 26
            print(val)
            if val < prev_val:
                return False
            prev_val = val
        return True
