import datetime

from InputReader import InputReader
from HdfcTransaction import HdfcTransaction


class HdfcInputReader(InputReader):
	def Read(self, fileLoc):
		if (fileLoc == ""):
			raise ValueError("'fileLoc' has an invalid value. ('" + fileLoc + "')")
		
		output = []
		lineCt = 0
		
		with open(fileLoc, 'r') as f:
			for line in f:			
				lineCt += 1
				
				if (lineCt <= 2): # First 2 lines of HDFC output are headers
					continue
					
				dateTime = line[0:11].strip()
				desc = line[12:133].strip()
				valueDate = line[134:143].strip()
				debitAmt = line[144:163].strip()
				creditAmt = line[164:183].strip()
				chqRefNumber = line[184:207].strip()
				closingBalance = line[208:223].strip()
				
				output.append(HdfcTransaction(
					datetime.datetime.strptime(dateTime, "%d/%m/%y"),
					desc,					
					datetime.datetime.strptime(valueDate, "%d/%m/%y"),
					float(debitAmt),
					float(creditAmt),
					chqRefNumber,
					float(closingBalance),
				))
		
		return output

