def is_monotonic(nums):
    increasing = True
    decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False
    
    return increasing or decreasing


nums1 = [1, 2, 2, 3]
print(is_monotonic(nums1)) 
nums2 = [6, 5, 4, 4]
print(is_monotonic(nums2))  

nums3 = [1, 3, 2]
print(is_monotonic(nums3))  







