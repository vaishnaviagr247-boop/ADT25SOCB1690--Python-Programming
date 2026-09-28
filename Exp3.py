class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Payment method must be implemented")


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# Create payment strategies
credit = CreditCardPayment()
paypal = PayPalPayment()

# Use Credit Card
payment = PaymentContext(credit)
payment.pay(1000)

# Change to PayPal
payment.set_strategy(paypal)
payment.pay(500)
