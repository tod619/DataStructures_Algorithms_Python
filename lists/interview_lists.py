# reverse a list
def reverse(nums:list) -> list:

    # Pointer for the first item
    start = 0

    # Pointer for the end of the array
    end = len(nums) - 1

    while end > start:
        # Swap the first item with the last item in the list
        nums[start], nums[end] = nums[end],nums[start]

        # increment the start pointer by 1
        start += 1

        # decrement the end pointer by 1
        end -= 1

    return nums

# Test reverse function
my_list = ["Start", 5, 2, 3, "End"]
print("***** Start: Reverse List Test *****")
print(f"Original list: {my_list}")
print(f"Reversed List: {reverse(my_list)}")
print("***** End: Reverse List Test *****\n")