class Customer:
    id_counter = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id_counter
        Customer.id_counter += 1

    @classmethod
    def get_next_id(cls):
        return cls.id_counter

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
