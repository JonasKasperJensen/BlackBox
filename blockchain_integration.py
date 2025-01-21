from web3 import Web3

# Connect to Avalanche C-Chain
blockchain_url = "https://api.avax.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(blockchain_url))

if web3.isConnected():
    print("Connected to Avalanche blockchain.")
else:
    raise ConnectionError("Failed to connect to Avalanche blockchain.")

# Check wallet balance
def check_balance(address):
    balance = web3.eth.get_balance(address)
    print(f"Wallet balance for {address}: {web3.fromWei(balance, 'ether')} AVAX")

# Example Wallet Check
example_wallet = "0xYourWalletAddressHere"
check_balance(example_wallet)
