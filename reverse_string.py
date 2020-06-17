
a=input('enter string')
def reverse():
    List=list(a)
    i=0
    j=len(List)-1
    while(i<j):
        if not List[i].isalpha():
            i+=1
        elif not List[j].isalpha():
            j-=1
        else:
            List[i],List[j]=List[j],List[i]
            i+=1
            j-=1
    return ''.join(List) 
print(reverse())       
            
        
 
      
        
                
    
    
    