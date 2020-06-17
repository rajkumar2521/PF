a=['raj','kumar']
v=0
c=0
for i in a:
    v=0
    c=0
    for j in i:
        
        if j in ['a', 'e', 'i', 'o', 'u']:
           
            v+=1
            
        else:
            c+=1
    print(v,c)
            
        