def get_edges(pollsters_stateedge_dict,state):
    #start writing your code here
    result_list=[]
    for country in pollsters_stateedge_dict:
        states = pollsters_stateedge_dict[country]
        if state in states.keys():
            result_list.append((country,states[state]))
        else:
            result_list.append((country,None))
    return result_list

# Part-2
def find_pollster_states(pollsters_stateedge_dict):
    #start writing your code here
    result_dict={}
    for country in pollsters_stateedge_dict:
        states = pollsters_stateedge_dict[country]
        result_dict[country] = list(states.keys())
    return result_dict

pollsters_stateedge_dict = { 
              "Gallup": { "WA": 7, "CA": 15, "UT": -30 }, 
              "SurveyUSA": { "CA": 14, "CO": 2, "CT": 13, "FL": 0 }, 
              "Omniscient": { "AK": -14.0, "WA": -2.3, "CA": 20.9 }
             } 

state='WA'
print("Pollsters, States and its edge details:",pollsters_stateedge_dict)
print("Given State:",state)
output=get_edges(pollsters_stateedge_dict,state)
print("Pollster Edge details for the given state:", output)  

output1=find_pollster_states(pollsters_stateedge_dict)
print("Pollster and their entire state details:",output1)