import requests
import json
import csv

file=requests.get("https://open-to-cors.s3.amazonaws.com/users.json")
jsonObj=json.loads(file.text)
keylist = list(jsonObj[0].keys())

for i in range(len(jsonObj)):
    if( '_id' in jsonObj[i].keys()):
        jsonObj[i]['id']=jsonObj[i]['_id']
        del jsonObj[i]['_id']

f = csv.writer(open("test.csv", "w"))
f.writerow(keylist)

def jsontocsv(input_json, output_path):
  keylist = []
  for key in jsonObj[0]:
    keylist.append(key)
    f = csv.writer(open(output_path, "w",newline=''))
    f.writerow(keylist)

  for record in jsonObj:
    currentrecord = []
    for key in keylist:
        currentrecord.append(record[key])
    f.writerow(currentrecord)
   
jsontocsv(jsonObj,'test.csv')
       
print('Check the desktop')
