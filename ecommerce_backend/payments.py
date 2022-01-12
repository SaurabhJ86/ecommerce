from dataclasses import dataclass
from abc import ABC, abstractmethod
from ecommerce_backend.Order import Order, OrderStatus

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self):
        pass



class DebitCardProcessor(PaymentProcessor):

    def __init__(self, sms_code):
        self.verified = False
        self.sms_code = sms_code
    
    def pay(self, order: Order):
        if not self.verified:
            raise Exception("Transaction is invalid")
        print(f"Initiating payment though Debit Card")
        print(f"Authenticating OTP sent..........")
        print("Authentication Verified.")
        order.status = OrderStatus.PAID
