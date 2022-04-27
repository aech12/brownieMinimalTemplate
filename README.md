Initial, minimalistic template based on https://github.com/smartcontractkit/full-blockchain-solidity-course-py#testing-basics

should fix* messed up dev and mainnet envs, should fix that

run tests
brownie test

run deploy
brownie run scripts/deploy.py
brownie run scripts/fund.py

run deploy (dev environment)
brownie run scripts/deploy.py --network ganache-local
