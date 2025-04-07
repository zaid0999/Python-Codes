grade_list=[['raresh','A'],
            ['suresh','B'],
            ['ramesh','A'],
            ['kishore','A'],
            ['rajesh','C']]

print(f'Student List {grade_list}')
gradeA_list=list(filter(lambda s:s[1]=='A',grade_list))
print(gradeA_list)
gradeB_list=list(filter(lambda s:s[1]=='B',grade_list))
print(gradeB_list)
gradeC_list=list(filter(lambda s:s[1]=='C',grade_list))
print(gradeC_list)