class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    test_cases = [121, -121, 10, 12321, 0]
    for case in test_cases:
        print(f"isPalindrome({case}) = {sol.isPalindrome(case)}")