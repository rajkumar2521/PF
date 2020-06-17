#PF-Prac-25
def list_of_count(word_list):
    l=[]
    for i in range(len(word_list)):
        l.append(len(word_list[i]))
        count_list=l
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))