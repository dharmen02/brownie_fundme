from brownie import FundMe
from scripts.helper_functions import get_account 

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})
def main():
    fund()
    withdraw()
    