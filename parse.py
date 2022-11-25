import re
import json

def extract_address(sentence):
    adresses = []
    # remove all non ascii characters
    sentence = re.sub(r'[^\x00-\x7F]+', '#', sentence)
    # remove all non alphanumeric characters
    sentence = re.sub(r'[^a-zA-Z0-9.-]+', '#', sentence)

    # if the sentence contains .eth
    if ".eth" in sentence:
        words = re.split("#", sentence)
        for word in words:
            if word.endswith(".eth"):
                adresses.append(word)
                
    return adresses

with open("a.json", "r") as f:
    data = json.load(f)
    for item in data:
        address = set(extract_address(item["name"]))
        address = address.union(extract_address(item["description"]))



        if(len(address) > 0):
            print(address, item["username"])



