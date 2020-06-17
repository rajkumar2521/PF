#PF-Prac-17
train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]

def get_train_name (train_no):
    for i in train_list:
        if i['train_no']==train_no:
            return i['name']
    return 'Invalid Train_no'        

def get_trains_for_day(day_of_run):
    list=[]
    if day_of_run!='Mo'and day_of_run!= 'Tu' and day_of_run!= 'We'and day_of_run!= 'Th' and day_of_run!= 'Fr' and day_of_run!= 'Sa':
        return 'Invalid day' 
        
    for i in train_list:
        for j in range(0,len(i['days_of_run'])):
            if (i['days_of_run'])[j]==day_of_run:
                list.append(i['train_no'])
    return list 

def get_total_fare(train_no,passenger_dict):
    c=0
    for i in train_list:
        if i['train_no']==train_no:
            for j in passenger_dict:
                if j=='sleeper':
                    c=c+i['sleeper_fare']*passenger_dict[j]
                else:
                    c=c+i['ac_fare']*passenger_dict[j]
                   
    return c                
print(get_train_name(25627))
print(get_trains_for_day("We"))
print(get_total_fare(25627,{"sleeper":10, "ac":10}))