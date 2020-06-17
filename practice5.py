#PF-Prac-5
def count_digits_letters(sentence):
   
    result_list=[]
    a=len(''.join([x for x in sentence if x.isalpha()]))
    b=len(''.join([x for x in sentence if x.isdigit()]))
    result_list.append(a)
    result_list.append(b)

    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))