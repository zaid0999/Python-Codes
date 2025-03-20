# Creating set using set() function 
# set() function is used to convert existing iterables into set type (OR) it alows to create or convert other colections into set type 

# Syntax1: set()   
# empty set 
# Syntax2: set(iterable)  This convert existing colection or iterable into set type





a=[10,20,30,10,20,30,40,50,30,40,50,]
b=set(a)
print(a)
print(b)

print()


c=list(b)
print(c)

print()

str1="abcabcdeabcde"
z=set(str1)
print(str1,type(str1))
print(z,type(z))


print()


s1=set(range(10,70,10))
print(s1)


s2=set((10,20,30,40,50))
print(s2,type(s2))



# Set is mutable colection but elements/values of set are immutable (OR) set alows only immutable objects.


print()


a={10,1.5,1+5j,"python",(10,20,30)}
print(a)


print()

