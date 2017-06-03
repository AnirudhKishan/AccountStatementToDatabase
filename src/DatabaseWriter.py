from abc import ABC, abstractmethod


class DatabaseWriter(ABC):
	
	def __init__(self, repository):
		self.Repository = repository
		
	@abstractmethod
	def Write(self, items):
		pass
