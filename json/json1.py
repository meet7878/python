import json
d={
    "course__name":"python",
    "fees":15000

}

f = json.dumps(d)

print(type(f))
print(f)

#module1