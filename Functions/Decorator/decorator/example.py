def draw_line(f):
    def print_line():
        print("*"*35)
        f()
        print("*"*35)
    return print_line

@draw_line
def display():
    print("PYTHON LANGUAGE")

@draw_line
def print_dict():
    stud_data={'naresh':'python',
               'ramesh':'java',
               'suresh':'oracle',
               'kishore':'mysql'}
    for name,course in stud_data.items():
        print(f'{name}==>{course}')
display()
print_dict()