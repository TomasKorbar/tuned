import unittest2

from tuned.utils.parsers.parser_options import ParserOptions

class ParserOptionsTestCase(unittest2.TestCase):

	def setUp(self):
		self._parser = ParserOptions()

	def test_get_bool(self):
		positive_values = ["1", "Y", "YES", "T", "TRUE"]
		negative_values = ["0", "N", "NO", "F", "FALSE"]

		for val in positive_values:
			self.assertEqual(self._parser.get_bool(val), True)

		for val in negative_values:
			self.assertEqual(self._parser.get_bool(val), False)

		self.assertEqual(self._parser.get_bool('bad_value'), 'bad_value')
