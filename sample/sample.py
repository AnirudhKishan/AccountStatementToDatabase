import sys
sys.path.append('../src')

from HdfcInputReader import HdfcInputReader
from HdfcSqliteDatabaseWriter import HdfcSqliteDatabaseWriter
from HdfcSqliteRepository import HdfcSqliteRepository


inputReader = HdfcInputReader()
transactions = inputReader.Read("input.txt")
	
hdfcSqliteRepository = HdfcSqliteRepository("db.sqlite")

databaseWriter = HdfcSqliteDatabaseWriter(hdfcSqliteRepository)
databaseWriter.Write(transactions)

