from web3 import Web3

# Replace with your own values
uuid = "2fa28b0b-08c4-408a-b78a-fcd42fee7859"
rpc_endpoint = "https://breakup.lac.tf/2fa28b0b-08c4-408a-b78a-fcd42fee7859"
private_key = "0x478ef3765b0caf14763e57321c7814c69b8afd387c83d7e9c214340f110fcea9"
setup_contract_address = "0x7c4C8FC305B009A3Ea344D3748457B8A262C41fe"

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider(rpc_endpoint))

with open("setup.abi", "r") as f:
  contract_abi = f.read()
print(contract_abi)

# Get the contract instance
setup_contract = w3.eth.contract(address=setup_contract_address, abi=contract_abi)

# Get the address of the default Ethereum account
address = w3.eth.account.privateKeyToAccount(private_key).address

# Call the "isSolved" function on the smart contract
is_solved = setup_contract.functions.isSolved().call()

# Check the result
if is_solved:
    print("The challenge is solved.")
else:
    print("The challenge is not yet solved.")