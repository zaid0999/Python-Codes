# Generator Function
def even_generator(start,stop):
    for num in range(start,stop):
        if num%2==0:
            yield num

a=even_generator(1,50) # Creating iterator object
for value in a:
    print(value,end=' ')