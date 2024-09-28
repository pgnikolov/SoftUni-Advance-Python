class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

account_details = input().split(", ")
pin_code = int(account_details[0])
balance = float(account_details[1])
age = int(account_details[2])

while True:
    command = input()

    if command == "End":
        break

    if command.startswith("Send Money"):
        _, money_str, entered_pin = command.split("#")
        money = float(money_str)
        entered_pin = int(entered_pin)

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        if entered_pin != pin_code:
            raise PINCodeError("Invalid PIN code")

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif command.startswith("Receive Money"):
        _, money_str = command.split("#")
        money = float(money_str)

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        balance += money / 2
        print(f"{money / 2:.2f} money went straight into the bank account")

