# Write a program to read scores n players into list

scores=[]
n=int(input("How Many players ?"))
for i in range(n):
    s=int(input(f'Player{i+1} Score :'))
    scores.append(s)
print(f'Scores are {scores}')
tot=0
for s in scores:
    tot=tot+s
print(f'Total score {tot}')

for i in range(n):
    if i==0:
        min_score=scores[i]
        max_score=scores[i]
    elif scores[i]>max_score:
        max_score=scores[i]
    elif scores[i]<min_score:
        min_score=scores[i]
    
print(f'Minimum score {min_score}')
print(f'Maximum score {max_score}')