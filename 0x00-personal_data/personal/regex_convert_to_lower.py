import re

# replacement function to convert uppercase letter to lowercase
def convert_to_lower(match_obj):
    if match_obj.group() is not None:
        return match_obj.group().lower()

# Original String
str = "Emma LOves PINEAPPLE DEssert and COCONUT Ice Cream"

# pass replacement function to re.sub()
res_str = re.sub(r"[A-Z]", convert_to_lower, str)
# String after replacement
print(res_str)
# Output 'Emma loves pineapple dessert and coconut Ice Cream'
