class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        
        for i in range(1, n + 1):
            ans_str = ""
            for key, value in fizz_buzz_dict.items():
                if i % key == 0:
                    ans_str += value
            if not ans_str:
                ans_str = str(i)
            ans.append(ans_str)
        return ans
