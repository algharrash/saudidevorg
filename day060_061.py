#python week 9 challenge

import json
import re

days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(json.dumps(days))

myStr = "data is the new oil"

x = re.search("data", myStr)
print(x.span())
