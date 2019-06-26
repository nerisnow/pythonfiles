import requests
def download (url,count):
    if "http" in url:
        r=requests.get(url)
        file=open(count,"wb")
        file.write(r.content)
        file.close()
    else:
        r = requests.get("https://youtube.com"+url)
        file = open(count, "wb")
        file.write(r.content)
        file.close()


res=requests.get("https://youtube.com")
#print(res.headers.keys())
lines=res.text.split(" ")

for line in lines:
    if("png" in line):
        qsplitted=line.split("\"")
        try:
            print(qsplitted[1])
            underscore=(qsplitted[1].split("/"))
            print(underscore[-1])
            download(qsplitted[1], underscore[-1])

        except Exception as e:
            print(e)


