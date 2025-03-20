grade_list=[['naresh','A'],
            ['sresh','B'],
            ['ramesh','A'],
            ['kishore','B'],
            ['rajesh','B'],
            ['kiran','C']]
grade_listA=[stud for stud in grade_list if stud[1]=='A']
grade_listB=[stud for stud in grade_list if stud[1]=='B']
grade_listC=[stud for stud in grade_list if stud[1]=='C']

print(grade_list)
print(grade_listA)
print(grade_listB)
print(grade_listC)