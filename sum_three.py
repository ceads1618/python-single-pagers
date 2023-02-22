# Create a function, sum_three, that given an array of integers *nums* and an integer *target*, returns the indices of three integers that add up to the target.
    # You can assume there will always be exactly one solution.
    # Each index must be unique; the order in which they are returned doesn't matter.
    # Return indices in an array.
    # Optize for time complexity.

def sum_three(nums, target):


test_case = list(range(-1200, -99)) + [19, 7, 4, 21, 38, 24, 20, 6, 3, 5, 23, 1, 8]
test_target = 21
# solution should return [1102, 1108, 1113] in any order.
print(sum_three(test_case, test_target))