import scrape
import wallet
import os

usernames = [
    "thedigitaldogs",
    "CryptoDickbutts",
    "0n1force",
    "kaijukingz",
    "overlord_xyz",
]

# create the out folder if it doesn't exist
if not os.path.exists("out"):
    os.makedirs("out")

print("Initiating scraping of followers")
scrape.pre_compute_followers(usernames)
print("Completed scraping of followers")

print("Initiating extracting wallet addresses")
wallet.extract_wallet_addresses(usernames)
