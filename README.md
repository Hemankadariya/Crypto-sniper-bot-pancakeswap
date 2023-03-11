# Crypto-sniper-bot-pancakeswap
It checks if there is liquidity on PancakeSwap for the specified token. If there is no liquidity, the code waits for 30 seconds and checks again. Once liquidity is added to the pair, the code proceeds to buy the specified amount of the token at the current market price, as in the original code.

#To run the Python code, you can follow these steps:

Install the required libraries: web3.

Copy code
``pip install web3``
Replace the placeholders in the code with your own values:

my_address: your address on Binance Smart Chain
my_private_key: your private key for my_address
abi: the ABI of the contract for the token you want to buy
token_contract_address: the contract address of the token you want to buy
factory_contract_address: the contract address of PancakeSwap's factory contract
router_contract_address: the contract address of PancakeSwap's router contract
Run the code in your Python environment:

Copy code
``python buy_token.py``
Make sure you are connected to the internet and have sufficient BNB balance in your wallet to cover the gas fees for the transaction. The code will output the transaction hash once the transaction is sent. You can monitor the status of the transaction on BscScan using the transaction hash.

# Note: To make the script running just add the while loop 
