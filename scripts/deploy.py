from brownie import FundMe, network
from scripts import helpers

net = network.show_active()


def main():
    print(f"Deploying to {net}")
    # deploy
    deploy = helpers.main()
    print(deploy)
    fundMe_contract = FundMe.deploy(
        deploy["priceFeed"],
        {"from": deploy["account"]},
        publish_source=deploy["verify"],
    )
    # deploy end
    print(f"store: {fundMe_contract.address}")
