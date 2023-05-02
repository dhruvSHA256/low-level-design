class _StripePayment:
    def makePayment(self):
        pass


class _Store:
    def makeStripePayment(self):
        stripePayment = _StripePayment()
        stripePayment.makePayment()


class IPayment:
    def makePayment(self):
        pass


class StripePayment(IPayment):
    def makePayment(self):
        print("making payment using stripe")


class Store:
    def makePayment(self, paymentObj: IPayment):
        paymentObj.makePayment()


store = Store()
stripePayment = StripePayment()
store.makePayment(stripePayment)
