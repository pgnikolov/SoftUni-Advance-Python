from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 50)

    def store_stats(self):

