import re

target_string = "Aisha Loves testing and bug bounty"
res_string = re.sub(r"\s", "", target_string)
print(target_string)
print(res_string)
