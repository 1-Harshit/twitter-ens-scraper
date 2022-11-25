from web3 import Web3
from ens import ENS

w3 = Web3(Web3.HTTPProvider("URL", request_kwargs={'timeout': 60}))
ns = ENS.fromWeb3(w3)


eth_address = ns.address('jasoncarver.eth')
print(eth_address)