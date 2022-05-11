class Query:
	def __init__(self, lowX, highX, lowY, highY):
		self._lowX = lowX
		self._highX = highX
		self._lowY = lowY
		self._highY = highY

	def getLowX(self):
		return self._lowX

	def getHighX(self):
		return self._highX
	
	def getLowY(self):
		return self._lowY
	
	def getHighY(self):
		return self._highY
