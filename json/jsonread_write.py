import json
from typing import final
file=open("posts.json","r")
x=file.read()
finaldata=json.loads(x)

#print(finaldata['id'])

for a in finaldata:

   print(a['id'])