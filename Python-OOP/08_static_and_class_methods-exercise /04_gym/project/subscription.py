class Subscription:
    id_counter = 1

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.id_counter
        Subscription.id_counter += 1

    @classmethod
    def get_next_id(cls):
        return cls.id_counter

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
