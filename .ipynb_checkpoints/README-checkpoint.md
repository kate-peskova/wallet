# wallet
Creating Multi-Blockchain Wallet in Python

## Multi-Blockchain Wallet in Python
In this project, we will install a hierarchical deterministic wallet using the Python hd-wallet-derive tool. Although this wallet can be universal, we would only concentrate on two coins – Bitcoin and Etherium on a test net. My operating system is MAC OS, thus, I will use the terminal and the corresponding Mac commands throughout this project.

To start out the project, we need to install the hd-wallet-derive tool in our project directory using the following set of commands:

```
git clone https://github.com/dan-da/hd-wallet-derive
  cd hd-wallet-derive
  curl https://getcomposer.org/installer -o installer.php
  php installer.php
  php composer.phar install
```

Once the hd-wallet tool is installed, we will create the _derive_ symlink running the following command:

```
ln -s hd-wallet-derive/hd-wallet-derive.php derive
```

To interact with the hd-wallet-tool, we will use Python. The links to the code files are listed below.

* [constants.py](python/constants.py)
* [wallet.py](python/wallet.py)

Activate the local network nodes. Please refer to this tutorial for details.

[Creating and running a locacal blockchain network tutorial](https://github.com/kate-peskova/hurricane-network/blob/main/README.md)


To interact with wallet.py through the terminal, start out with the following commands and replace them with the appropriate parameters:

```
>>> from wallet import *
>>> account=priv_key_to_account(COIN, 'PRIVATE KEY')
>>> transaction=send_tx(COIN, account, ADDRESS, amount)
```

We will use a block explorer to watch the BTC transactions on the address.

![](Screenshots/btc-transaction.png)

To confirm an ETH transaction, we will use MyCrypto app.

![](Screenshots/eth-transaction.png)


