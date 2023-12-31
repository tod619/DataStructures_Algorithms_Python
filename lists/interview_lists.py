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

def is_palindrome_python(s:str) -> bool:

    if s == s[::-1]:
        return True
    
    return False


print("***** Start: Palindrome Test *****")
print(f"Is racecar a palindrome?: {is_palindrome_python('racecar')}")
print(f"Is horse a palindrome?: {is_palindrome_python('horse')}")
print("***** End: Palindrome Test *****\n")


# Reverse an integer value
def reverse_integer(n:int) -> int:
    # your implementation goes here
    result = str(n)
    
    result = result[::-1]
    
    result = int(result)
    
    return result

print("***** Start: Reverse Int *****")
print(f"1245 reversed is: {reverse_integer(1245)}")
print("***** End: Reverse Int *****\n")

# Check if 2 strings are anagrams of each other
def is_anagram(str1:str, str2:str ) -> bool:
    if len(str1) != len(str2):
        return False
    
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True
