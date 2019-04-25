class ParserOptions():

	def __init__(self):
		pass

	def get_bool(self, value):
		"""Return True if string value can be considered as True otherwise False

		if determination fails then original value will be returned
		Positional arguments:
		value -- value which should be parsed to boolean
		"""
		if type(value) is bool:
			return value
		v = str(value).upper().strip()
		return {"1":True,"Y":True, "YES":True, "T":True, "TRUE":True, "0":False, "N":False, "NO":False, "F":False, "FALSE":False}.get(v, value)
