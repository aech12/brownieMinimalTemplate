from operator import imod
from brownie import accounts, Store
from random import randint


def test_main():
    account = accounts[0]
    store_con = Store.deploy({"from": account})
    initialFavNumber = store_con.retrieve()
    assert initialFavNumber == 0

    randomInt = randint(-2000, 2000)
    store_con.store(randomInt)
    assert store_con.retrieve() == randomInt
