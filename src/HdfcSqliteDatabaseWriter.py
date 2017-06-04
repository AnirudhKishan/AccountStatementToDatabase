from DatabaseWriter import DatabaseWriter
from SqlCommand import SqlCommand

class HdfcSqliteDatabaseWriter(DatabaseWriter):
	def __init__(self, hdfcRepository):
		super().__init__(hdfcRepository)

	def Write(self, items):
		for item in items:
			if (self.ExistsInDb(item)):
				continue
		
			self.InsertFromHdfcTransaction(item)
			
	def InsertFromHdfcTransaction(self, hdfcTransaction):
		query_1 = "INSERT INTO [Transactions] ([Timestamp], [Amount], [Description]) VALUES (:timestamp, :amount, :description);"
		params_1 = {
			'timestamp': hdfcTransaction.Timestamp.isoformat(),
			'amount': str(hdfcTransaction.Amount),
			'description': 	hdfcTransaction.Description,
		}
		self.Repository.ExecuteCommand(SqlCommand(query_1, params_1))
		
		query_2 = "INSERT INTO [HdfcTransactions] ([TransactionId], [ValueDate], [DebitAmount], [CreditAmount], [ChqRefNumber], [ClosingBalance]) VALUES ((SELECT seq FROM [sqlite_sequence] WHERE [name]='Transactions'), :valueDate, :debitAmount, :creditAmount, :chqRefNumber, :closingBalance);"
		params_2 = {
			'valueDate': hdfcTransaction.ValueDate.isoformat(),
			'debitAmount': hdfcTransaction.DebitAmount,
			'creditAmount': hdfcTransaction.CreditAmount,
			'chqRefNumber': hdfcTransaction.ChqRefNumber,
			'closingBalance': hdfcTransaction.ClosingBalance,
		}
		self.Repository.ExecuteCommand(SqlCommand(query_2, params_2))

	def ExistsInDb(self, hdfcTransaction):
		query_1 = "SELECT * FROM [Transactions] WHERE [Timestamp]=:timestamp AND [Amount]=:amount AND [Description]=:description;"
		params_1 = {
			'timestamp': hdfcTransaction.Timestamp.isoformat(),
			'amount': str(hdfcTransaction.Amount),
			'description': 	hdfcTransaction.Description,
		}
		result_1 = self.Repository.ExecuteQuery(SqlCommand(query_1, params_1))
		
		query_2 = "SELECT * FROM [HdfcTransactions] WHERE [ValueDate]=:valueDate AND [DebitAmount]=:debitAmount AND [CreditAmount]=:creditAmount AND [ChqRefNumber]=:chqRefNumber AND [ClosingBalance]=:closingBalance;"
		params_2 = {
			'valueDate': hdfcTransaction.ValueDate.isoformat(),
			'debitAmount': hdfcTransaction.DebitAmount,
			'creditAmount': hdfcTransaction.CreditAmount,
			'chqRefNumber': hdfcTransaction.ChqRefNumber,
			'closingBalance': hdfcTransaction.ClosingBalance,
		}
		result_2 = self.Repository.ExecuteQuery(SqlCommand(query_2, params_2))
		
		return ((len(result_1) > 0) and len(result_2) > 0) # i.e. the whole transaction already exists in DB
