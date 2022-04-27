from brownie import accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
START_PRICE = 2000


def deployInLocal():
    account = accounts[0]

    priceFeed = (
        MockV3Aggregator[-1].address
        if len(MockV3Aggregator) > 0
        else MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(START_PRICE, "ether"), {"from": account}
        ).address
    )

    verify = False
    return {"account": account, "priceFeed": priceFeed, "verify": verify}


def deploy(net):
    account = accounts.add(config["wallets"]["private_key"])

    priceFeed = config["networks"][net]["eth_usd_priceFeed"]

    publish = True
    return {"account": account, "priceFeed": priceFeed, "verify": verify}
