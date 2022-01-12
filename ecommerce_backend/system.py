from dataclasses import dataclass

from ecommerce_backend.Order import Order
from ecommerce_backend.user_profile import UserType

@dataclass
class ProcessOrder:

    def __init__(self):
        self.free_delivery: bool = True

    def process_order(self, order: Order) -> None:
        if order.user.user_type == UserType.PRIME:
            print(f"Order would be delivered within 5-7 days")
        elif order.user.user_type == UserType.PRIVILEGED:
            print("Order would be delivered with 3-5 days")
        elif order.user.user_type == UserType.UBER:
            print("Order would be delivered with 1-2 days")
        elif order.user.user_type == UserType.NORMAL:
            print("Order would be delivered with 7-10 days")
            self.free_delivery = False