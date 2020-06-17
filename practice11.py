#PF-Prac-11
def find_upper_and_lower(sentence):
    list=[]
    c1=0
    c2=0
    for i in range(len(sentence)):
        if sentence[i]>='A' and sentence[i]<='Z':
            c1+=1
        elif sentence[i]>='a' and sentence[i]<='z':
            c2+=1
    list.append(c1)        
    list.append(c2)
    result_list=list        
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))