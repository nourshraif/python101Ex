def ZeroSum(nums):
    newlist = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                newlist.append([nums[i], nums[left], nums[right]])
                
              
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
                
    return newlist



list=[-1,0,1,2,-1,-4]
print(ZeroSum(list))