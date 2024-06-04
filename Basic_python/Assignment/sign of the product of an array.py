def sign_func(nums):
    negative_count = 0
    for num in nums:
        if num < 0:
            negative_count += 1
        elif num == 0:
            return 0
    
    
    return -1 if negative_count % 2 else 1


nums1 = [-1, -2, -3, -4, 3, 2, 1]
print(sign_func(nums1)) 

nums2 = [1, 5, 0, 2, -3]
print(sign_func(nums2))  

nums3 = [-1, 1, -1, 1, -1]
print(sign_func(nums3))  






