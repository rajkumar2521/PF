
def printPascal(n): 

    for i in range(1, n + 1): 
        C = 1; 
        for j in range(1, i + 1): 
            print(C, end = " "); 
            C = int(C * (i - j) / j); 
        print(""); 


n = 6; 
printPascal(n); 


