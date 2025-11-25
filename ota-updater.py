import requests,sys
File = sys.argv[1]
url="http://linux-dev-arch.github.io/ota/" + File
print("Getting file...")
try:
    req = requests.get(url)
    with open(File,"w") as f:
        f.write(req.text)
    print("Successfully updated")
except:
    print("An error occured! Check file name or internet connection")
