from ens import ENS
from web3 import Web3
import os
import json
import parse


def get_ns_instance():
    # To set your environment variables in your terminal run the following line:
    # export 'PROVIDER_URL'='<your_bhttp_provider_url>'
    provider_url = os.environ.get("PROVIDER_URL")
    w3 = Web3(Web3.HTTPProvider(provider_url, request_kwargs={"timeout": 60}))
    ns = ENS.fromWeb3(w3)

    return ns


def get_followers(username):
    with open("out/" + username + ".json") as f:
        followers = json.load(f)
    return followers


def get_wallet_address(ns, enseth):
    wallet_address = ""
    for ens in enseth:
        if wallet_address == "":
            wallet_address = ns.address(ens)
        else:
            wallet_address += " | " + ns.address(ens)
    return wallet_address


def save_followers_wallet(ns, followers, username):
    next_print = 5000  # print every 5000/10000 followers
    with open("out/" + username + ".csv", "a") as f:
        for i, follower in enumerate(followers):
            # Print progress
            if i > next_print:
                print("Extracted {} follower's wallet addresses".format(i))
                next_print += 10000
            # Extract wallet ens
            address = parse.extract_address_from_item(follower)
            if len(address) == 0:
                continue
            # Get wallet address
            wallet_address = get_wallet_address(ns, address)
            f.write("{},{},{}\n".format(username, follower["username"], wallet_address))


# CSV Header: Account, Follower Account, Wallet Address
def extract_wallet_addresses(usernames):
    ns = get_ns_instance()

    print("Initiating extracting wallet addresses")
    for username in usernames:
        followers = get_followers(username)
        # Print csv headers
        with open("out/" + username + ".csv", "a") as f:
            f.write("Account,Follower Account,Wallet Address\n")
        # Extract wallet addresses and save to csv
        save_followers_wallet(ns, followers, username)
    print("Completed extracting wallet addresses")
