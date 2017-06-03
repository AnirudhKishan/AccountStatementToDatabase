from Transaction import Transaction


class HdfcTransaction(Transaction):
	def __init__(self, timestamp, description, valueDate, debitAmount, creditAmount, chqRefNumber, closingBalance):
		self.ValueDate = valueDate
		self.DebitAmount = debitAmount
		self.CreditAmount = creditAmount
		self.ChqRefNumber = chqRefNumber
		self.ClosingBalance = closingBalance
		
		if (self.CreditAmount == 0.0):
			amount = -1 * self.DebitAmount
		else:
			amount = self.CreditAmount
		
		super(HdfcTransaction, self).__init__(timestamp, amount, description)
