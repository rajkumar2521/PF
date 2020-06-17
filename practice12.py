
subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
sentence=[]
for i in range (len(subjects)):
    for j in range (len(verbs)):
        for k in range (len(objects)):
            outlist=(subjects[i]+" "+verbs[j]+' '+objects[k])
            sentence.append(outlist)
print(sentence)
    
    
    