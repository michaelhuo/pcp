from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def Bubble(nums: List[int]) -> List[int]:
            for k in range(len(nums)):
                for i in range(len(nums) - k - 1):
                    if nums[i+1] < nums[i]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
            return nums
        def Insert(nums: List[int]) -> List[int]:
            for i in range(1, len(nums)):
                n = nums[i]
                j = i
                while j > 0 and nums[j-1] > n:
                    nums[j] = nums[j - 1]
                    j -= 1
                nums[j] = n

            return nums

        def Shell(nums: List[int]) -> List[int]:
            if not nums:
                return []
            N = len(nums)
            # step = N
            step = 1
            # Knuth's interval
            while step < N // 3:
                step = step * 3 + 1

            while step > 0:
                # step = step // 2
                for k in range(0, step):
                    for i in range(k + step, N, step):
                        n = nums[i]
                        j = i
                        while j > step - 1 and nums[j - step] > n:
                            nums[j] = nums[j - step]
                            j -= step
                        nums[j] = n
                step = (step - 1) // 3
            return nums

        def Selection(nums: List[int]) -> List[int]:
            if not nums:
                return []
            N = len(nums)
            for i in range(N - 1):
                minimum = i
                for j in range(i + 1, N):
                    if nums[j] < nums[minimum]:
                        minimum = j
                if minimum != i:
                    nums[i], nums[minimum] = nums[minimum], nums[i]
            return nums
        def merge_sort(nums: List[int]) -> List[int]:
            N = len(nums)
            if N < 2:
                return nums
            mid = N // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            result = []
            i, j = 0, 0
            while i < len(left) or j < len(right):
                if i == len(left) or j < len(right) and right[j] <= left[i]:
                    result.append(right[j])
                    j += 1
                elif j == len(right) or i < len(left) and left[i] <= right[j]:
                    result.append(left[i])
                    i += 1

            return result

        def quick_sort1(nums: List[int], low: int, high: int) -> None:

            if low >= high or high - low > len(nums):
                return
            pivot = partition(nums, low, high)
            quick_sort(nums, low, pivot)
            quick_sort(nums, pivot + 1, high)


        def partition1(nums: List[int], low: int, high: int) -> int:
            import random
            pivot = nums[random.randrange(low, high + 1)]

            (i, j) = (low - 1, high + 1)
            while True:
                while True:
                    i = i + 1
                    if nums[i] >= pivot:
                        break
                while True:
                    j = j - 1
                    if nums[j] <= pivot:
                        break

                if i >= j:
                    return j
                
                nums[i], nums[j] = nums[j], nums[i]
        def quick_sort(nums: List[int], low: int, high: int) -> None:
            if len(nums) < 2 or low >= high or high - low > len(nums):
                return

            pivot = partition(nums, low, high)
            quick_sort(nums, low, pivot - 1)
            quick_sort(nums, pivot + 1, high)

        def partition(nums: List[int], low: int, high: int) -> int:
            # if high - low < 1:
            #     return low
            import random
            pivot_index = random.randrange(low, high + 1)
            if pivot_index != high:
                nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
            pivot = nums[high]
            i = low            
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = i + 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        quick_sort(nums, 0, len(nums) - 1)
        return nums

def main():
    import random
    # nums = [5,2,3,1]
    nums = [ random.randrange(-50000, 50000) for _ in range(10)]
    print(nums)
    print(Solution().sortArray(nums))

if __name__ == "__main__":
    main()
