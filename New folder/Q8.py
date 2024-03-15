max_score = None
max_index = None
scores = [0,1,2,3,4,5,6,7,8,9,11]
for i in range(len(scores)):
    if max_score == None or max_score < scores[i]:
        max_score = scores[i]
        max_index = i
