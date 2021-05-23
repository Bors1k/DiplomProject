import re
string = '{"Description": "3854bc50-bbcc-11eb-8529-0242ac130003", "AppUID":"dwada", "GOST":"8328-75"}'
Info = {}
Info["description"] = (re.search('"Description": "\w*\-\w*\-\w*\-\w*\-\w*"',string)).group(0)
Info["description"] = re.findall('\w*\-\w*\-\w*\-\w*\-\w*',Info["description"])[0]

Info["GOST"] = (re.search('"GOST":"[^"]*"',string)).group(0) 
Info["GOST"] = re.findall('"[^"]*"',Info["GOST"])[1]
Info["GOST"] = str(Info["GOST"]).replace("\"","")
print(Info)
