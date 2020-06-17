#PF-Prac-9
def generate_dict(number):
    list1=[]
    list2=[]
    for i in range(1,number+1):
        list1.append(i*i)
    for j in range(1,number+1):
        list2.append(j)
        new_dict=dict(zip(list2,list1))
    return new_dict

number=4
print(generate_dict(number))