import re

# replacement function to convert uppercase word to lowercase
# and lowercase word to uppercase
def convert_case(match_obj):
    if match_obj.group(1) is not None:
        return match_obj.group(1).lower()
    if match_obj.group(2) is not None:
        return match_obj.group(2).upper()

# Original String
str = "EMMA loves PINEAPPLE dessert and COCONUT ice CREAM"
print(str)
# group 1 [A-Z]+ matches uppercase words
# group 2 [a-z]+ matches lowercase words
# pass replacement function 'convert_case' to re.sub()
res_str = re.sub(r"([A-Z]+)|([a-z]+)", convert_case, str)

# String after replacement
print(res_str)
# Output 'emma LOVES pineapple DESSERT AND coconut ICE cream'
