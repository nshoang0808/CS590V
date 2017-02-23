import re
import os

# Open file table 2A
readfile = "Table 2A.csv"
with open(os.path.join('data', readfile)) as f:
    content = f.readlines()
content = [x.strip() for x in content]

writefile = "Table 2A.csv"
with open(os.path.join('data', writefile),'w') as f:
    for line in content:
        if len(re.split('","|,"|",', line)) == 6 or len([x for x in line.split(",") if x != ""]) == 6:
            print(line, file = f)

# Open file table 2J
readfile = "Table 2J.csv"
with open(os.path.join('data', readfile)) as f:
    content = f.readlines()
content = [x.strip() for x in content]

writefile = "Table 2J.csv"
with open(os.path.join('data', writefile),'w') as f:
    for line in content:
        if len(re.split('","|,"|",', line)) == 6 or len([x for x in line.split(",") if x != ""]) == 6:
            print(line, file = f)
