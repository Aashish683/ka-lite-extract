import json

dict={}

with open('prettyTopics.json','r') as infile:
    dict = json.load(infile)

remove_key = "child_data"

res = {}

def remove(dict):
    dict.pop(remove_key,None)
    if('children' in dict):
        for dictionary in dict['children']:
            remove(dictionary)

remove(dict)

with open('topicData.json', 'w') as outfile:
    json.dump(dict, outfile,indent=2)
