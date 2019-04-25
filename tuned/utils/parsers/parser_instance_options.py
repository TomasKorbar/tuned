import tuned.logs
from tuned.utils.parsers.parser_options import ParserOptions

log = tuned.logs.get()

class ParserInstanceOptions(ParserOptions):

	def __init__(self, plugin):
		self._plugin = plugin

	def _instance_management_options(self):
		return {"dynamic": self._plugin.dynamic_tuning_enabled_by_default()}

	def _instance_management_options_parsers(self):
		return {"dynamic": self.get_bool}

	def _parse_instance_option(self, key, value):
		return self._instance_management_options_parsers()[key](value)

	def parse_options(self, options):
		"""Check options contained in profile and divide them

		Options will be checked if their names are known and then
		divided into tuple containing tuning options for plugin and
		instance management options for instance

		Positional arguments:
		options -- dict containing all options from profile for plugin instance

		Return value:
			tuple (tuning_options, instance_management_options)
		"""
		# TODO: _has_dynamic_options is a hack
		plug = self._plugin
		tuning_effective = plug._get_config_options().copy()
		instance_effective = self._instance_management_options()
		for key in options:
			if key in instance_effective.keys():
				val = options[key]
				instance_effective[key] = self._parse_instance_option(key, val)
			elif (key in tuning_effective or
					plug._has_dynamic_options):
				tuning_effective[key] = options[key]
			else:
				log.warning("Unknown option '%s' for plugin '%s'." % (key,
					plug.__class__.__name__))
		return (tuning_effective, instance_effective)
