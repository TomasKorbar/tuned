import unittest2

from tuned.utils.parsers.parser_instance_options import ParserInstanceOptions
from tuned.plugins.base import Plugin

class ParserInstanceOptionsTestCase(unittest2.TestCase):

	def setUp(self):
		self._parser = ParserInstanceOptions(DummyPlugin)

	def test_parse_options(self):
		opts = {"dynamic":"1", "opt1":"val1", "wrong":"option"}

		# We need only one test because this test checks all possible
		# combinations of options
		# overriden default value of option, unoverriden value, bad value and
		# conversion of numeric value to boolean
		(tuning_options, instance_options) = self._parser.parse_options(opts)
		self.assertEqual(instance_options, {"dynamic":True})
		self.assertEqual(tuning_options, {"opt1":"val1", "opt2":"def2"})
		# this test emits warning log message with bad name of plugin
		# that is expected and it is side effect of use of plugin class and not
		# its instance

class DummyPlugin(Plugin):
	# has dynamic options is not normally a class variable but i do not
	# want to create instance and all its dependencies because of one variable
	_has_dynamic_options = False

	@classmethod
	def _get_config_options(cls):
		return {"opt1":"def1", "opt2":"def2"}
