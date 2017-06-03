import sqlite3
from abc import ABC, abstractmethod

from SqlCommand import SqlCommand


class SqliteRepository(ABC):
	TRANSACTIONS_TABLE_CREATE_SQL = 'CREATE TABLE IF NOT EXISTS "Transactions" ("Id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "Timestamp" TEXT NOT NULL, "Amount" REAL NOT NULL, "Description" TEXT NOT NULL DEFAULT (\'\'));'
	
	def __init__(self, path):	
		self.Path = path
		self.EnsureDbSanity()
		
	def EnsureDbSanity(self):
		command = SqlCommand(SqliteRepository.TRANSACTIONS_TABLE_CREATE_SQL)
	
		self.ExecuteCommand(command)
		
	def ExecuteCommand(self, command):
		conn = sqlite3.connect(self.Path)
		
		cur = conn.cursor()
		cur.execute(command.Query, command.Params)
		conn.commit()
		
		conn.close()
		
	def ExecuteQuery(self, command):
		conn = sqlite3.connect(self.Path)
		
		cur = conn.cursor()
		cur.execute(command.Query, command.Params)
		conn.commit()
		
		output = cur.fetchall()
		
		conn.close()
		
		return output
