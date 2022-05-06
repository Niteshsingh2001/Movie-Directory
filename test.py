import requests as req
import pprint
import json

url = f"http://www.omdbapi.com/?apikey=afb102e2&t=RRR"
# url = f"http://www.omdbapi.com/?apikey=afb102e2t=RRR"

data = req.get(url)
print(data)
x = json.loads(data.content)
pprint.pprint(x.keys())

print(x["Response"])
if "Error" in x.keys():
        pprint.pprint(x["Response"])
else:
        pprint.pprint("xyz")
