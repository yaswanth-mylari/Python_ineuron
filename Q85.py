#Write a Python program to find cumulative sum of a list.
def cumulative_sum(nums):
    return [sum(nums[:i+1]) for i in range(len(nums))]
numbers = [1, 2, 3, 4, 5]
cumulative_result = cumulative_sum(numbers)
print(cumulative_result)
