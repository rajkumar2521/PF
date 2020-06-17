#PF-Prac-7
def seed_no(number,ref_no):
    
    product=number
    while (number>0):
        
   
        rem=int(number%10)
        
        product=product*rem
        number=int(number/10)
    if product==ref_no:
        return True
    else:
        return False
        
        
number=123
ref_no=738
print(seed_no(number,ref_no))