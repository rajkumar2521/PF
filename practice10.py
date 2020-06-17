#PF-Prac-10
def string_both_ends(input_string):
    if len(input_string)<2:
        return -1
    elif len(input_string)==2:
        return input_string+input_string
    else:
        return input_string[:2]+input_string[-2:]
input_string="w3resource"
print(string_both_ends(input_string))