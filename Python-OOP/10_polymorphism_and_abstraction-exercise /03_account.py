class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __lt__(self, obj):
        return self.balance < obj.balance

    def __le__(self, obj):
        return self.balance <= obj.balance

    def __eq__(self, obj):
        return self.balance == obj.balance

    def __ne__(self, obj):
        return self.balance != obj.balance

    def __gt__(self, obj):
        return self.balance > obj.balance

    def __ge__(self, obj):
        return self.balance >= obj.balance

    def __add__(self, obj):
        concatenate_two_accounts = Account(f"{self.owner}&{obj.owner}", self.amount + obj.amount)
        concatenate_two_accounts._transactions = self._transactions + obj._transactions
        return concatenate_two_accounts
