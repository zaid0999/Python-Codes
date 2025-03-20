# Write a program to remove ith character from string 


str1="programming"
print(f'Before Deleting: {str1}')
i=6
a=list(str1)
del a[i]
str2=''.join(a)
print(f'After Deleting: {str2}')