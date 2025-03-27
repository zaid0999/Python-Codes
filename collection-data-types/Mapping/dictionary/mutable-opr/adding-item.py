# Adding item within dictionary

# Syntax:  dictionary-name[key]=value 

# This syntax is used to perform two operations 
# 1. Adding item 
# 2. Updating value of given key (OR) updating value 

# If given key not exists within dictionary it wi l add key with value 
# If given key exists within dictionary it wi l replace value of given key


# Example

d1={}
print(d1,type(d1))

d1[1]=10
print(d1)

print()

d1[2]=20
print(d1)

print()

d1[3]=30
print(d1)

print()

d1[2]=42
print(d1)



# Example:

# Write a program to read scores on "n" players
# each player is having two values 
# name and runs 
# store these value in dictionary 
# find total score, maximum score, minimum score 

n=int(input("How many Players? "))
players={}
for i in range(n):
    pname=input("Player Name ")
    score=int(input("Score "))
    if pname in players:
        print(f'{pname} Exists')
    else:
        players[pname]=score

tot=0
max_score=None
min_score=None
t1=None
t2=None
for pname,score in players.items():
    print(f'{pname}==>{score}')
    tot+=score
    if max_score==None and min_score==None:
        max_score,min_score=score,score
    elif score>max_score:
        max_score=score
        t1=(pname,score)
    elif score<min_score:
        min_score=score
        t2=(pname,score)
print(f'Total Score {tot}')
print(f'Maximum Score {t1}')
print(f'Minimum Score {t2}')