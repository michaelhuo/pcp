import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for n in nums:
            if n in num_counts:
                num_counts[n] += 1
            else:
                num_counts[n] = 1
        count_lists = {}
        counts = []
        for n, c in num_counts.items():
            if c in count_lists:
                count_lists[c].append(n)
            else:
                count_lists[c] = [n,]
                counts.append(c)
        heapq.heapify(counts)
        lst = heapq.nlargest(k, counts)
        m = 0
        answer = []
        for c in lst:
            l = count_lists[c]
            m += len(l)
            answer += count_lists[c]
            if m == k:
                break
        return answer
    
