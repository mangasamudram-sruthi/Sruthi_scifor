def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    
    # Fill the remaining part with zeros
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


nums1 = [0, 1, 0, 3, 12]
move_zeros(nums1)
print(nums1) 

nums2 = [0]
move_zeros(nums2)
print(nums2)  






# In[ ]:




