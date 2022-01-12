""" Transaction would be done from here """

from ecommerce_backend.Order import Order
from ecommerce_backend.payments import DebitCardProcessor
from ecommerce_backend.system import ProcessOrder
from ecommerce_backend.user_profile import User, UserType


def main():
    #Create a user
    user = User(name="Julia Benez",email="julia@yahoo.com",phone="9091RDO3",status=True,user_type=UserType.PRIME)

    #Place a Order
    order = Order(item="Jabra Bluetooth Earphones",quantity=1,price=7000,user=user)

    #Select Payment Process
    payment = DebitCardProcessor(201)
    payment.verified = True
    payment.pay(order=order)

    #Process Order
    process_order = ProcessOrder()
    process_order.process_order(order)


if __name__ == "__main__":
    main()