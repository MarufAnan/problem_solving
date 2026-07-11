# Removing All Whitespace in a String

import re

string = "m a r   u f"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)

