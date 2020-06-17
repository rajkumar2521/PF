#PF-Prac-32
def check_squares(number):
    
    for i in range(1,number):
        for j in range(1,number):
            if i*i+j*j==number:
                return True
            j+=1    
        i+=1        
         
    return False    
number=84
print(check_squares(number))
