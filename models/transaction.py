class Transaction:
    def __init__(self, transaction_date, merchant, tag, transaction_amount, id=None):
        self.transaction_date = transaction_date
        self.merchant = merchant
        self.tag = tag
        self.transaction_amount = transaction_amount
        self.id = id
