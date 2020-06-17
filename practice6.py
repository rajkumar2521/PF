def list123(nums):
    c=0
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]-1:
            c+=1
        if c==2 or (nums[i+1]==3 and i==len(nums)-2):
            return True
        if nums[i]!=nums[i+1]-1:
            c=0
       
    return False            
        
        
        
nums=[2,1,2,3,8,5]
print(list123(nums))






