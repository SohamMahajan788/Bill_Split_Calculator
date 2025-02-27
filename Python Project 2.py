from colorama import Fore, Style

print(Style.BRIGHT + Fore.RED + "💰Welcome to the Bill Split Calculator!💰" + Style.RESET_ALL)
bill = float(input(Fore.YELLOW + "What was the total bill? 💲" + Style.RESET_ALL))
tip = int(input(Fore.YELLOW + "What percentage tip would you like to give? (e.g., 0, 10, 12, or 15)? " + Style.RESET_ALL))
people = int(input(Fore.YELLOW + "How many people going to split the bill? " + Style.RESET_ALL))
bill_plus_tip = bill + (bill * tip / 100)
split = round(bill_plus_tip / people, 2)
print(Style.BRIGHT + Fore.GREEN + f"Each person should pay: 💲" + str(split) + Style.RESET_ALL)
