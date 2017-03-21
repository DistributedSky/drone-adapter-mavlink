from web3 import Web3
import json, os

abi = '[{"constant":false,"inputs":[{"name":"_ipfs_hash","type":"string"}],"name":"acquire","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_ipfs_hash","type":"string"}],"name":"get","outputs":[{"name":"","type":"address"},{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_ipfs_hash","type":"string"}],"name":"release","outputs":[],"payable":false,"type":"function"}]'

class Route:
    def __init__(self, ipfs_hash):
        web3 = Web3(Web3.RPCProvider(host=os.environ['WEB3_HOST']))
        pk_manager = Web3.PrivateKeySigningManager(web3._requestManager)
        pk_manager.register_private_key(os.environ['WEB3_PRIV_KEY'])
        web3.setManager(pk_manager)
        self.contract = web3.eth.contract(abi=json.loads(abi), address=os.environ['ROUTE_MUTEX'])
        self.ipfs_hash = ipfs_hash

    def acquire(self):
        return self.contract.transact().acquire(self.ipfs_hash)

    def release(self):
        return self.contract.transact().release(self.ipfs_hash)
