from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient


class SphereRestaurantApp:
    WAITER_TYPES = {'FullTimeWaiter': FullTimeWaiter, 'HalfTimeWaiter': HalfTimeWaiter}
    CLIENT_TYPES = {'VIPClient': VIPClient, 'RegularClient': RegularClient}
    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITER_TYPES.keys():
            return f"{waiter_type} is not a recognized waiter type."

        ex_waiter = self._get_waiter_by_name(waiter_name)
        if ex_waiter:
            return f"{waiter_name} is already on the staff."

        new_waiter = self.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."


    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES.keys():
            return f"{client_type} is not a recognized client type."

        ex_client = self._get_client_by_name(client_name)
        if ex_client:
            return f"{client_name} is already a client."

        new_client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter_ = self._get_waiter_by_name(waiter_name)
        if not waiter_:
            return f"No waiter found with the name {waiter_name}."

        return waiter_.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client_ = self._get_client_by_name(client_name)
        if not client_:
            return f"{client_name} is not a registered client."

        result = client_.earning_points(order_amount)
        return f"{client_name} earned {result} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client_ = self._get_client_by_name(client_name)
        if not client_:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        discount_percentage, remaining_points = client_.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        total_client_points = sum(client.points for client in self.clients)
        clients_count = len(self.clients)

        report = f"$$ Monthly Report $$\n"
        report += f"Total Earnings: ${total_earnings:.2f}\n"
        report += f"Total Clients Unused Points: {total_client_points}\n"
        report += f"Total Clients Count: {clients_count}\n"
        report += "** Waiter Details **\n"

        for waiter in sorted_waiters:
            report += str(waiter) + "\n"

        return report


    def _get_waiter_by_name(self, name: str):
        for w in self.waiters:
            if w.name == name:
                return w

    def _get_client_by_name(self, client_name: str):
        for client in self.clients:
            if client.name == client_name:
                return client
