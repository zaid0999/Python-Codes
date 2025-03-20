#  Write a program to accept percentage and display the Category according to the following criteria:
# Percentage              Category
#   <40                    Failed
# >=40&<55                 Fair
# >=55&<65                 Good
# >=65                     Excellent


marks=int(input("Enter The Marks "))
if marks<40:
    print("Failed")
elif marks>=40 and marks<55:
    print("Fair")
elif marks>=55 and marks<65:
    print("Good")
else:
    marks<=65
    print("Excellent")