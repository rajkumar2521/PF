#PF-Prac-2
def bracket_pattern(input_str):
    
    cl=0
    cr=0
    
    for i in range(len(input_str)):
        if input_str[i]=='(':
            cl+=1
        else:
            cr+=1
    if cl==cr:
        return True
    else:
        return False
            
            
input_str="(())("
print(bracket_pattern(input_str))