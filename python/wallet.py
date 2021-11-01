# Importing dependencies
import subprocess
import json
import os
from web3 import Web3, Account
from bit import wif_to_key
from dotenv import load_dotenv
from bit.network import NetworkAPI
from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware

# Loading and setting environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Importing constants.py and necessary functions from bit and web3

from constants import BTC, ETH, BTCTEST
w3 = Web3(Web3.HTTPProvider(os.getenv('ETH_NETWORK')))
 
# Creating a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive=10, format='json'):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --cols=all --coin={coin} --numderive={numderive} --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Creating a dictionary object called coins to store the output from `derive_wallets`.
coins = {
    BTCTEST: derive_wallets(mnemonic, coin=BTCTEST),
    ETH: derive_wallets(mnemonic, coin=ETH),
}


# Creating a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin in [BTC, BTCTEST]:
        return wif_to_key(priv_key)
    if coin in [ETH]:
        return Account.privateKeyToAccount(priv_key)

# Creating a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin in [BTC, BTCTEST]:
        return [(to, amount, BTC)]
    if coin in [ETH]:
     
  #      gasEstimate = w3.eth.estimateGas(
  #          {'from': account.address, 'to': to, 'value': amount}
  #      )
        return {
            'from': account.address,
            'to': to,
            'value': amount,
            'gasPrice': w3.eth.gasPrice,
            'gas': 1000000,
            'nonce': w3.eth.getTransactionCount(account.address),
            'chainId': 177
        }

# Creating a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    raw_tx = create_tx(coin, account, to, amount)
    if coin in [BTC, BTCTEST]:
        return account.send(raw_tx)
    if coin in [ETH]:
        signed_tx = account.sign_transaction(raw_tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)


