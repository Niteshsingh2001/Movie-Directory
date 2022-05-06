import requests as req
import pprint
import json

url = f"http://www.omdbapi.com/?apikey=afb102e2&t=RRR"
# url = f"http://www.omdbapi.com/?apikey=afb102e2t=RRR"

data = req.get(url)
pprint.pprint(json.loads(data.content))