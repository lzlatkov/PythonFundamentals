# https://pastebin.com/TGAtYCvp

def get_products():
    return Storage.storage


class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            self.capacity -= 1
            Storage.storage.append(product)

