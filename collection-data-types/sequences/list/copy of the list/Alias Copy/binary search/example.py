# Searching element in list using binary search



n=int(input("How many values? "))
a=[]
for i in range(n):
    value=int(input("Enter Value :"))
    a.append(value)
a.sort()
value=int(input("Enter value to search :"))
low=0
high=len(a)-1
while low<=high:
    mid=(low+high)//2
    if a[mid]==value:
        print(f'Element Found {mid}')
        break
    elif value<a[mid]:
        high=mid-1
    elif value>a[mid]:
        low=mid+1
else:
    print("Element Not Found")