import contract
from pyteal import *
from beaker import *

# Compiling the contract
contract.MyApplication().dump("artifacts")

account = sandbox.get_accounts().pop()

# Creates the application Client
app_client = client.ApplicationClient(
  client = sandbox.get_algod_client(),
  app = contract.MyApplication(version=7),
  signer = account.signer,
)

# Creates the smart contract on-chain
app_id, app_addr, txid = app_client.create()

# Saves the app ID on a file to use it later
open("./artifacts/app_id", "w").write(str(app_id))

print(
  f"""Deployed app in txid {txid}
    App ID: {app_id} 
    Address: {app_addr} 
"""
)


