from collections import Counter


def count_odd_even(nums: list[int]) -> tuple[int, int]:
    odd = [num % 2 for num in nums]
    return sum(odd), len(nums) - sum(odd)


if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    odd_1, even_1 = count_odd_even(nums[::2])
    odd_2, even_2 = count_odd_even(nums[1::2])
    