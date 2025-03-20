# str.rpartition(sep) 
# Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator



s1="a,b,c,d,e"
t1=s1.rpartition(",")
print(t1)


print()


t2=s1.partition(",")
print(t2)


print()


t3=s1.rpartition(":")
print(t3)