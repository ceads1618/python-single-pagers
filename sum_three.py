# Create a function, sum_three, that given a list of unique integers *nums* and an integer *target*, returns the indices of three integers that add up to the target
    # You can assume there will always be exactly one solution
    # Each index must be unique; the order in which they are returned doesn't matter
    # Return indices in a list
    # Optize for time complexity

# Pseudocode
    # Create an object to store values to remove the need for a third nested loop
    # No need to account for the same integer being in two separate indices since uniqueness of original list is established
    # However, holding indices in a tuple at int. key and ensuring all indices are unique before returning would accomplish this
    # Ex. {7: (0, 1, 2)} could return solution [0, 1, 2] for target 21 of nums [7, 7, 7]
    # Iterate through the nums list to add integer and corresponding index
    # Iterate through list twice to create all possible combinations of values
    # First iteration should stop 1 index short of the end since the second loop will access that value for the final combination
        # Second loop will always start at the index after the parent loop since the prior combinations have already been checked
            # Determine value necessary to equal target
            # Check if the new target is in third index dict.
            # If it is, check to ensure the index value stored isn't the same as either current two indices. Avoids using same element
                # return all three indices in a list
    # No need for a default value since we are guaranteed always having one solution.

def sum_three(nums, target):
    third_index = {}

    for index in range(len(nums)):
        third_index[nums[index]] = index

    for index in range(len(nums)-1):
        for index2 in range(index+1, len(nums)):
            new_target = target - nums[index] - nums[index2]
            if new_target in third_index and third_index[new_target] != index and third_index[new_target] != index2:
                index3 = third_index[new_target]
                return [index, index2, index3]

test_case = list(range(-1200, -99)) + [19, 7, 4, 21, 38, 24, 20, 6, 3, 5, 23, 1, 8]
test_target = 21
# solution should return [1102, 1108, 1113] in any order
print(sum_three(test_case, test_target))