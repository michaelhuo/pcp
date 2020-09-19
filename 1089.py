class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return
        length = len(arr)
        last = length - 1
        # zero_count = sum([ 1 for n in arr if n == 0])
        # if zero_count == 0:
        #    return
        i = 0
        zero_count = 0
        while True:
            if i + zero_count == last:
                arr[last] = arr[i]
                last -= 1
                i -= 1
                break
            elif i + zero_count == last - 1:
                if arr[i] == 0:
                    zero_count += 1
                    arr[last - 1] = 0
                    arr[last] = 0
                    last -= 2
                    i -= 1 
                    break
            else:
                if arr[i] == 0:                    
                    zero_count += 1
            i += 1
            
        j = last
        while i >= 0:
            if arr[i] != 0:
                arr[j] = arr[i]
                j -= 1
            else:
                arr[j], arr[j - 1] = 0, 0
                j -= 2            
            i -= 1
        # arr[length - zero_count:] = []
        