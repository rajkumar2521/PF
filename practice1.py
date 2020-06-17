#PF-Prac-3


prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
new_dict={}

for i in prices:
    if prices[i]>200:
        new_dict.update({i:prices[i]})
        
        
print(new_dict)
