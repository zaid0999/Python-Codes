print()

# Course Enq Application


course={'python':'6000',
        'java':'5000',
        'oracle':'4000',
        '.net':'4500'}

cname=input("Enter Course Name to Find fees: ")
if cname in course:
    fee=course[cname]
    print(f'{cname}==>{fee}')
else:
    print(f'{cname} not found')



print()