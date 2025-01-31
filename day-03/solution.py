
# i never liked regex, and now i know why!

import re
with open('input.txt') as file:
    text = file.read()

# part 1:
def mult(s):
    x,y = s[4:-1].split(",")
    return int(x)*int(y)

match = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", text)
sum([mult(p) for p in match])

# part 2:
parts = ("do()" + text).split("don't()")
selection = "".join([p.split("do()", 1)[1] if "do()" in p else "" for p in parts])
match = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", selection)
sum([mult(p) for p in match])
