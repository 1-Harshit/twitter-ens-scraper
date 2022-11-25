import re

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

def extract_address_from_item(item):
    # Simple text in name and description(bio)
    address = set(extract_address(item["name"]))
    address = address.union(extract_address(item["description"]))

    # Links in name and description(bio)
    if "entities" in item:
        entities = item["entities"]
        if "description" in entities and "urls" in entities["description"]:
            urls = entities["description"]["urls"]
            for url in urls:
                if "expanded_url" in url:
                    address = address.union(extract_address(url["expanded_url"]))
        # if "url" in entities and "urls" in entities["url"]:
        #     urls = entities["url"]["urls"]
        #     for url in urls:
        #         if "expanded_url" in url:
        #             address = address.union(extract_address(url["expanded_url"]))
    return address



