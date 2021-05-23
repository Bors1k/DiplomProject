import re
string = '{"Description": "wadaw"}'
Info = {}
Info["description"] = (re.search('"Description": "\w+"',string)).group(0)
Info["description"] = re.findall('\w+',Info["description"])[1]
print(Info)

