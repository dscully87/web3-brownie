import os

from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    # Transactions and Calls are handled correctly by brownie
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(15, {"from": account})
    # In brownie if making a transaction you always have to pass in a from account
    transaction.wait()
    updated_stored_value = simple_storage.retrieve()


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
