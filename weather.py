import  json
import requests
r=requests.get("https://www.metaweather.com/api/location/search/?lattlong=84.1240,28.3949")
jobj=json.loads(r.text)
print(jobj[0]['distance'])
woe=jobj[2]['woeid']
print(woe)
r1=requests.get("https://www.metaweather.com/api/location/{}/".format(woe))
jobr=json.loads(r1.text)
pout=jobr['consolidated_weather']
print(pout[0]['id'])