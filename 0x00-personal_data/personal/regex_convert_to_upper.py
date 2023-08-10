import re

# replacement function to convert lowercase to uppercase
def convert_to_upper(match_obj):
    if match_obj.group() is not None:
        return match_obj.group().upper()

# Original String
str = "Emma LOves PINEAPPLE DEssert and COCONUT Ice Cream"

# pass replacement function to re.sub()
res_str = re.sub(r"[a-z]", convert_to_upper, str)
# String after replacement
print(res_str)
# Output 'Emma loves pineapple dessert and coconut Ice Cream'
