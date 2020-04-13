from urllib import request
import json

content = request.urlopen("https://jsonblob.com/api/593e0bfd-7d77-11ea-9563-4b410f96c8ea").read()
print(json.loads(content.decode()))