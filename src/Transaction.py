import datetime


class Transaction:
	
	def __init__(self, timestamp, amount, description):
		self.Timestamp = timestamp
		self.Amount = amount
		self.Description = description

