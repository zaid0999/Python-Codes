# Python – Convert Snake case to Pascal case 
'''Converting a string from snake case to 
Pascal case involves transforming a format where 
words are separated by underscores into a 
single string where each word starts with an 
uppercase letter, including the first word.'''



str1="studen_name"
a=str1.split("_")
# b=[s.capitalize() for s in a]
# str2=''.join(b)
# print(str1)
# print(str2)

str2=''.join([s.capitalize() for s in a])
print(str1)
print(str2)