import contract
from pyteal import *
from beaker import *

# Open the file where we're saving the app ID
text_file = open("./artifacts/app_id", "r")
app_id = int(text_file.read())
text_file.close()

# Get the accounts trough the sandbox client
account = sandbox.get_accounts().pop()

# Create the Application Client
app_client = client.ApplicationClient(
  client = sandbox.get_algod_client(),
  app = contract.MyApplication(version=7),
  app_id = app_id,
  signer = account.signer,
)

## Call a method
result = app_client.call(contract.MyApplication.hello, name="Silvio")
print(result.return_value)

