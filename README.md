# python

from colorama import Fore
from colorama import Style

def main(balance):
    print(f"\n{Fore.CYAN}You currently have {Fore.YELLOW}${balance} {Fore.CYAN}in your account.{Style.RESET_ALL}\n")
    deposit_withdraw = input(f"{Fore.CYAN}Would you like to make a {Fore.YELLOW}deposit {Fore.CYAN}or {Fore.YELLOW}withdraw{Fore.CYAN}?{Fore.GREEN}\n")
    if deposit_withdraw == "deposit":
        return deposit(balance)
    elif deposit_withdraw == "withdraw":
        return withdraw(balance)
    else:
        return print(f"{Fore.RED}You must either choose deposit or withdraw.")

def deposit(balance):
    deposit_amount = input(f"{Style.RESET_ALL}{Fore.CYAN}How much money would you like to deposit into your account?{Style.RESET_ALL}\n")
    if deposit_amount.isdigit():
        return process_deposit(deposit_amount, balance)
    else:
        print(f"\nERROR:\n{Fore.RED}You must enter a valid integer.{Style.RESET_ALL}\n")

def process_deposit(deposit_amount, balance):
    if int(deposit_amount) <= int(1000000000):
        print(f"\n{Fore.GREEN}You have successfully deposited {Fore.YELLOW}${deposit_amount} {Fore.GREEN}into your account.{Style.RESET_ALL}\n")
        balance = int(balance) + int(deposit_amount)
        # print(f"{Fore.GREEN}You now have $" + str(balance) + " in your account.{Style.RESET_ALL}\n")
        print(f"{Fore.MAGENTA}Your new balance is now {Fore.YELLOW}$" + str(balance) + f"{Fore.BLUE}.\n")
        return main(balance)
    else:
        print(f"\n{Fore.RED}ERROR:\n{Fore.GREEN}An error has occured, try again with a lower amount (1 billion).{Style.RESET_ALL}\n")
        return main(balance)

def withdraw(balance):
    withdraw_amount = input(f"{Style.RESET_ALL}{Fore.CYAN}How much money would you like to withdraw from your account?{Style.RESET_ALL}\n")
    if withdraw_amount.isdigit():
        return process_withdraw(withdraw_amount, balance)
    else:
        print(f"\nERROR:\n{Fore.RED}You must enter a valid integer.{Style.RESET_ALL}\n")

def process_withdraw(withdraw_amount, balance):
    if int(balance) <= 0:
        return print(f"\n{Fore.RED}SYSTEM:\n{Fore.GREEN}You have no money left in your bank account!{Style.RESET_ALL}\n")
    if int(balance) >= int(withdraw_amount):
        print(f"\n{Fore.GREEN}You have successfully withdrawn {Fore.YELLOW}${withdraw_amount} {Fore.GREEN}from your account.{Style.RESET_ALL}\n")
        balance = int(balance) - int(withdraw_amount)
        # print(f"{Fore.GREEN}You now have $" + str(balance) + " in your account.{Style.RESET_ALL}\n")
        print(f"{Fore.MAGENTA}Your new balance is now {Fore.YELLOW}$" + str(balance) + f"{Fore.BLUE}.\n")
        if int(balance) <= 0:
            return print(f"\n{Fore.RED}SYSTEM:\n{Fore.GREEN}You have no money left in your bank account!{Style.RESET_ALL}\n")
        else:
            return main(balance)
    else:
        print(f"\n{Fore.RED}ERROR:\n{Fore.GREEN}You do not have enough money in your account to withdraw that amount.{Style.RESET_ALL}\n")
        return main(balance)

balance = 1000
main(balance)
