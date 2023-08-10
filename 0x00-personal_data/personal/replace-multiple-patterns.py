import re

# Original string
student_names = "Emma-Kelly Jessa Joy Scott-Joe Jerry"

# replace two pattern at the same time
# use OR (|) to separate two pattern
res = re.sub(r"(\s)|(-)", ",", student_names)
print(res)
# Output 'Emma,Kelly,Jessa,Joy,Scott,Joe,Jerry'
