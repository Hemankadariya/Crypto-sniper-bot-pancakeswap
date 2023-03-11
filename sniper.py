from web3 import Web3
import time

# connect to Binance Smart Chain using Web3
w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org:443'))

# set token and amount to buy
token_contract_address = '0x...'  # replace with the contract address of the token you want to buy
amount_to_buy = 100  # replace with the amount of the token you want to buy

# check for liquidity on PancakeSwap
while True:
    try:
        # get the contract instance of the token
        token_contract = w3.eth.contract(address=token_contract_address, abi=abi)

        # get the pair address for the token on PancakeSwap
        pair_address = factory_contract.functions.getPair(token_contract_address, w3.eth.contract(address=wbnb_address, abi=abi).address).call()

        # check the liquidity of the pair
        reserves = pair_contract.functions.getReserves().call()
        if reserves[0] > 0 and reserves[1] > 0:
            print('Liquidity added to the pair!')
            break
        else:
            print('Waiting for liquidity to be added...')
            time.sleep(30)
    except Exception as e:
        print(f'Error checking for liquidity: {e}')
        time.sleep(30)

# buy the token on PancakeSwap
try:
    # get the contract instance of the token and the PancakeSwap router
    token_contract = w3.eth.contract(address=token_contract_address, abi=abi)
    router_contract = w3.eth.contract(address=router_address, abi=abi)

    # get the current price of the token on PancakeSwap
    path = [token_contract_address, w3.eth.contract(address=wbnb_address, abi=abi).address]
    amount_out = router_contract.functions.getAmountsOut(amount_to_buy, path).call()
    amount_out_min = amount_out[1] - (amount_out[1] // 10)

    # build the transaction to buy the token
    tx = {
        'from': my_address,
        'to': router_address,
        'value': amount_to_buy,
        'gas': 210000,
        'gasPrice': Web3.toWei('5', 'gwei'),
        'nonce': w3.eth.getTransactionCount(my_address)
    }

    # add the buy token function call to the transaction
    tx['data'] = router_contract.encodeABI(fn_name='swapExactETHForTokens', args=[amount_out_min, path, my_address, int(time.time()) + 1000])

    # sign and send the transaction to buy the token
    signed_tx = w3.eth.account.signTransaction(tx, private_key=my_private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f'Transaction sent to buy {amount_to_buy} tokens with hash: {Web3.toHex(tx_hash)}')
except Exception as e:
    print(f'Error buying tokens: {e}')
