from typing import List

import sys
print(sys.getrecursionlimit())
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins = [-1] * len(nums)
        ballons = []
        return self._maxCoins(nums, 0, len(nums), coins, ballons)

    def _maxCoins(self, nums: List[int], left: int, right: int, coins: List[int], ballons: List[int]) -> int:
        max_coin = 0
        max_index = -1
        length = right - left
        for i in range(length):
            l = i - 1
            while l >= left and coins[l] != -1:
                l -= 1
            if l < left:
                cl = 1
            else:
                cl = nums[l]

            r = i + 1
            while r <= right - 1 and coins[r] != -1:
                r += 1
            if r == right:
                cr = 1
            else:
                cr = nums[r]

            c = nums[i] * cl * cr

            if l == -1 and r == length:
                max_index = i
                max_coin = c
                coins[i] = c
                ballons.append(max_index)
                print(ballons)
                print(coins)
                return sum(coins)

            if c > max_coin:
                max_coin = c
                max_index = i

        coins[max_index] = max_coin
        coin_current = sum(coins)
        coin_left = self._maxCoins(nums, 0, max_index, coins, ballons)
        coin_right = self._maxCoins(nums, max_index + 1, len(nums),coins, ballons)
        return max(coin_current, coin_left, coin_right)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins = [-1] * len(nums)
        ballons = []
        length = len(nums)
        left = 0
        right = length
        for _ in range(length):
            max_coin = -1
            max_index = -1
            for i in range(length):
                if coins[i] != -1:
                    continue
                l = i - 1
                while l >= left and coins[l] != -1:
                    l -= 1
                if l < left:
                    cl = 1
                else:
                    cl = nums[l]

                r = i + 1
                while r <= right - 1 and coins[r] != -1:
                    r += 1
                if r == right:
                    cr = 1
                else:
                    cr = nums[r]

                c = nums[i] * cl * cr

                print(i, c)

                if c > max_coin or c == max_coin and nums[i] < nums[max_index]:
                    max_coin = c
                    max_index = i

            coins[max_index] = max_coin
            ballons.append(max_index)
            print(coins)
            print(ballons)
            print("---")

        return sum(coins)


if __name__ == "__main__":
    print(Solution().maxCoins([1,3,5]))