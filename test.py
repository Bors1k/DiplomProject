import re
string = '{"Description": "3854bc50-bbcc-11eb-8529-0242ac130003", "AppUID":"dwada", "GOST":"8328-75","TYPE":"1 - 262000k"}'
Info = {}
Info["description"] = (re.search('"Description": "\w*\-\w*\-\w*\-\w*\-\w*"',string)).group(0)
Info["description"] = re.findall('\w*\-\w*\-\w*\-\w*\-\w*',Info["description"])[0]

Info["TYPE"] = (re.search('"TYPE":"[^"]*"',string)).group(0)
print(Info["TYPE"])
Info["TYPE"] = re.findall('"[^"]*"',Info["TYPE"])[1] 
print(Info["TYPE"])
Info["TYPE"] = str(Info["TYPE"]).replace("\"","") 
print(Info["TYPE"])
# print(Info)
