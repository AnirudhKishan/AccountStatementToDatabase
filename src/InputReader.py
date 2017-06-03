from abc import ABC, abstractmethod


class InputReader(ABC):	
	@abstractmethod
	def Read(self, fileLoc):
		pass
