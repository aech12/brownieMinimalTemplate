from brownie import accounts, config, MockV3Aggregator, network
from web3 import Web3

FORKED_ENVS = ["mainnet-forked"]
LOCAL_ENVS = ["development", "ganache-local"]
net = network.show_active()
DECIMALS = 8
START_PRICE = 2e11


def checkCurrentNet() -> str:
    if net in LOCAL_ENVS:
        return "dev"
    elif net in FORKED_ENVS:
        return "forked"
    else:
        return "mainnet"


def getAccount():
    if checkCurrentNet() in ["dev", "forked"]:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["private_key"])


def deployInLocal():
    account = getAccount()

    priceFeed = (
        MockV3Aggregator[-1].address
        if len(MockV3Aggregator) > 0
        else MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(START_PRICE, "ether"), {"from": account}
        ).address
    )

    return {"account": account, "priceFeed": priceFeed, "verify": False}


def deploy():
    account = getAccount()

    priceFeed = config["networks"][net]["eth_usd_priceFeed"]

    return {"account": account, "priceFeed": priceFeed, "verify": True}


def main():
    currentNet = checkCurrentNet()
    if currentNet == "dev":
        return deployInLocal()
    else:
        return deploy()
