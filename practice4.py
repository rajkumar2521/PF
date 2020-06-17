#PF-Prac-4
def find_nine(nums):
   
        if len(nums)<=5:
            if 9 in nums:
                return True
            return False    
        
    

nums=[1,9,4,5,6]
print(find_nine(nums))