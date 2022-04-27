from brownie import FundMe
from scripts import helpers


def fundContract():
    fund_contract = FundMe[-1]
    account = helpers.getAccount()
    fee = fund_contract.getEntranceFee()
    print(fee)
    fund_contract.fund({"from": account, "value": fee + 1000})
    return fund_contract

def withdrawFromContract():
    fund_contract = FundMe[-1]
    account = helpers.getAccount()
    fund_contract.withdraw({"from": account})
    return fund_contract