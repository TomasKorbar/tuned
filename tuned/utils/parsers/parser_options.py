class ParserOptions():

	def __init__(self):
		pass

	def option_bool(self, value):
		"""Return True if string value can be considered as True otherwise False

		Positional arguments:
		value -- value which should be parsed to boolean
		"""
		if type(value) is bool:
			return value
		value = str(value).lower()
		return value == "true" or value == "1"
