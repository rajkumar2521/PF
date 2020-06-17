def Palindrome(num):
    if str(num)==str(num)[::-1]:
        return num+num
    else:
        while(str(num)!=str(num)[::-1]):
            num=num+int(str(num)[::-1])
    return num        
    
    
print(Palindrome(4))   
