import json
import requests

r=requests.get("https://www.metaweather.com/api/location/search/?lattlong=28.3949,84.1240")

jobj=json.loads(r.text)
id=0
for hey in jobj:
    print("id{}=".format(id)+str(hey))
    id=id+1
inp=input("enter the id ")
a=jobj[int(inp)]
print(a["woeid"])
b=a["woeid"]
s=requests.get("https://www.metaweather.com/api/location/{}/".format(b))
joj=json.loads(s.text)
c=joj["consolidated_weather"]
#print(c[0])
print("The weateher state name is {}".format(c[0]['weather_state_name']))
print("The min temp is={}".format(c[0]['min_temp']))