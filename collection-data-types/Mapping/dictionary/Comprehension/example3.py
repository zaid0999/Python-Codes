# Filter data based on condition

grade_dict={'naresh':'A', 
            'suresh':'B', 
            'ramesh':'A', 
            'kishore':'A', 
            'rajesh':'C'}
print(grade_dict)
grade_dicta={name:grade for name,grade in grade_dict.items() if grade=='A'}
grade_dictb={name:grade for name,grade in grade_dict.items() if grade=='B'}
grade_dictc={name:grade for name,grade in grade_dict.items() if grade=="C"}
print(grade_dicta)
print(grade_dictb)
print(grade_dictc)