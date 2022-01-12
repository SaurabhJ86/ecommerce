""" This class will define the Order data """
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

from ecommerce_backend.user_profile import User

class OrderStatus(Enum):
    TRANSIT = auto()
    PAID = auto
    INITIATED = auto()
    RETURNED = auto()
    DELIVERED = auto()
    CANCELLED = auto()


@dataclass
class Order:
    item: str = ""
    quantity: int = 0
    price: int = 0
    order_id: str = ""
    time: datetime =  datetime.today()
    user: User = None
    status: OrderStatus = OrderStatus.INITIATED

    def compute_bill(self):
        return self.price * self.item


