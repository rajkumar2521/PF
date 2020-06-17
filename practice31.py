
def sum_of_elements(num_list,number):
    n=len(num_list)
    result_sum=0
    i=0
    for i in range(n-1):
        if i==0:
            if(num_list[i+1]!=number and num_list[i]!=number):
                result_sum+=num_list[i]
        else:
            if(num_list[i+1]!=number and num_list[i]!=number and num_list[i-1]!=number):
                result_sum+=num_list[i]
    i+=1           
    if(num_list[i]!=number and num_list[i-1]!=number):
            result_sum+=num_list[i]
        
  
    return result_sum            
num_list=[7,2,7]
number=7
print(sum_of_elements(num_list, number))