#PF-Prac-15
def check_22(num_list):
    c=0
    for i in range(len(num_list)-1):
        if num_list[i]==2 and num_list[i+1]==2:
            return True
        else:
            return False
            
   
           
    
print(check_22([2,2,3,2,5,2,2]))