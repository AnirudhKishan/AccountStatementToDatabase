from SqliteRepository import SqliteRepository
from SqlCommand import SqlCommand


class HdfcSqliteRepository(SqliteRepository):
	HDFC_TRANSACTIONS_TABLE_CREATE_SQL = 'CREATE TABLE IF NOT EXISTS "HdfcTransactions" ("Id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "TransactionId" INTEGER NOT NULL, "ValueDate" TEXT NOT NULL, "DebitAmount" REAL NOT NULL, "CreditAmount" REAL NOT NULL, "ChqRefNumber" TEXT NOT NULL, "ClosingBalance" REAL NOT NULL);'
	
	def __init__(self, path):
		super().__init__(path)
		
	def EnsureDbSanity(self):
		super().EnsureDbSanity()
		
		command = SqlCommand(HdfcSqliteRepository.HDFC_TRANSACTIONS_TABLE_CREATE_SQL)
		self.ExecuteCommand(command)

