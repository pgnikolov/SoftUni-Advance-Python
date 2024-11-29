from collections import defaultdict
from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 50)

    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        model_stats = defaultdict(lambda: {'count': 0, 'total_price': 0})

        for product in self.products:
            model_stats[product.model]['count'] += 1
            model_stats[product.model]['total_price'] += product.price

        toys_info = []
        for model in sorted(model_stats.keys()):
            count = model_stats[model]['count']
            avg_price = model_stats[model]['total_price'] / count
            toys_info.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        return (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                f"{self.get_estimated_profit()}\n"
                f"**Toys for sale:\n" +
                "\n".join(toys_info))